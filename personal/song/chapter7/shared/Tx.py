from io import BytesIO
import requests
from shared.Utility import hash256, int_to_little_endian, little_endian_to_int, read_varint, encode_varint
from shared.Script import Script

SIGHASH_ALL = 1

class Tx:
    def __init__(self, version, tx_ins, tx_outs, locktime, testnet=False):
        self.version = version
        self.tx_ins = tx_ins
        self.tx_outs = tx_outs
        self.locktime = locktime
        self.testnet = testnet
    
    def __repr__(self):
        tx_ins = ''
        for tx_in in self.tx_ins:
            tx_ins += tx_in.__repr__() + '\n'
        tx_outs = ''
        for tx_out in self.tx_outs:
            tx_outs += tx_out.__repr__() + '\n'
        return 'tx: {}\nversion: {}\ntx_ins:\n{}tx_outs:\n{}locktime: {}'.format(
            self.id(),
            self.version,
            tx_ins,
            tx_outs,
            self.locktime,
        )
    
    def id(self): 
        return self.hash().hex()

    def hash(self):
        #return hash256(b'sup')
        return hash256(self.serialize())[::-1]

    def serialize(self):
        result = int_to_little_endian(self.version, 4)
        result += encode_varint(len(self.tx_ins))
        for tx_in in self.tx_ins:
            result += tx_in.serialize()
        result += encode_varint(len(self.tx_outs))
        for tx_out in self.tx_outs:
            result += tx_out.serialize()
        result += int_to_little_endian(self.locktime, 4)
        return result
    
    def fee(self, testnet=False):
        value_of_inputs = 0
        for tx_in in self.tx_ins:
            value_of_inputs += tx_in.value(testnet=False)
        value_of_outputs = 0
        for tx_out in self.tx_outs:
            value_of_outputs += tx_out.amount
        return value_of_inputs - value_of_outputs

    def sig_hash(self, input_index):
        modified_tx = int_to_little_endian(self.version, 4)
        modified_tx += encode_varint(len(self.tx_ins))
        # empty ScriptSig from all inputs.  Replace ScriptSig with ScriptPubKey for just input being signed
        for i, tx_in in enumerate(self.tx_ins): 
            if i == input_index:
                modified_tx += TxIn(tx_in.prev_tx, tx_in.prev_index, tx_in.script_pubkey(self.testnet), tx_in.sequence).serialize()
            else:
                modified_tx += TxIn(tx_in.prev_tx, tx_in.prev_index, None, tx_in.sequence).serialize()
        modified_tx += encode_varint(len(self.tx_outs))
        for tx_out in self.tx_outs:
            modified_tx += tx_out.serialize()
        modified_tx += int_to_little_endian(self.locktime, 4)
        # append hash type
        modified_tx += int_to_little_endian(SIGHASH_ALL, 4)
        h256 = hash256(modified_tx)
        return int.from_bytes(h256, 'big')

    def verify_input(self, input_index):
        z = self.sig_hash(input_index)
        tx_in = self.tx_ins[input_index]
        prev_tx_pubkey = tx_in.script_pubkey(self.testnet)
        combined_script = tx_in.script_sig + prev_tx_pubkey
        return combined_script.evaluate(z)

    def verify(self):
        if self.fee() < 0:
            return False
        for i in range(len(self.tx_ins)):
            if not self.verify_input(i):
                return False
        return True


    @classmethod
    def parse(cls, stream, testnet=False):
        version = little_endian_to_int(stream.read(4))
        num_inputs = read_varint(stream)
        inputs = []
        for input in range(num_inputs):
            inputs.append(TxIn.parse(stream))
        outputs = []
        num_outputs = read_varint(stream)
        for ouptut in range(num_outputs):
            outputs.append(TxOut.parse(stream))
        locktime = little_endian_to_int(stream.read(4))
        return cls(version, inputs, outputs, locktime, testnet=testnet)


class TxIn:
    def __init__(self, prev_tx, prev_index, script_sig=None, sequence=0xffffffff):
        self.prev_tx = prev_tx
        self.prev_index = prev_index
        if script_sig is None:
            self.script_sig = Script()
        else:
            self.script_sig = script_sig
        self.sequence = sequence

    def __repr__(self):
        return '{}:{}'.format(self.prev_tx.hex(), self.prev_index)

    def serialize(self):
        result = self.prev_tx[::-1]
        result += int_to_little_endian(self.prev_index, 4)
        result += self.script_sig.serialize()
        result += int_to_little_endian(self.sequence, 4)
        return result

    def fetch_tx(self, testnet=False):
        return TxFetcher.fetch(self.prev_tx.hex(), testnet=testnet)

    def value(self, testnet=False):
        tx =  self.fetch_tx(testnet=testnet)
        return tx.tx_outs[self.prev_index].amount

    def script_pubkey(self, testnet=False):
        tx = self.fetch_tx(testnet=testnet)
        return tx.tx_outs[self.prev_index].script_pubkey

    @classmethod
    def parse(cls, stream):
        prev_tx_id = stream.read(32)[::-1]
        prev_tx_index = little_endian_to_int(stream.read(4))
        script_sig = Script.parse(stream)
        sequence = little_endian_to_int(stream.read(4))
        return cls(prev_tx_id, prev_tx_index, script_sig, sequence)


class TxOut:
    def __init__(self, amount, script_pubkey):
        self.amount = amount
        self.script_pubkey = script_pubkey

    def __repr__(self):
        return '{}:{}'.format(self.amount, self.script_pubkey)

    def serialize(self):
        result = int_to_little_endian(self.amount, 8)
        result += self.script_pubkey.serialize()
        return result

    @classmethod
    def parse(cls, stream):
        amount = little_endian_to_int(stream.read(8))
        script_pubkey = Script.parse(stream)
        return cls(amount, script_pubkey)
    
class TxFetcher:
    cache = {}

    @classmethod
    def get_url(cls, testnet=False):
        if testnet:
            return 'https://blockstream.info/testnet/api'
        else:
            return 'https://blockstream.info/api'
    
    @classmethod
    def fetch(cls, tx_id, testnet=False, fresh=False):
        # get raw transaction by id, parse it then verify the hash matches the original id you fetched
        if fresh or (tx_id not in cls.cache):
            url = '{}/tx/{}/hex'.format(cls.get_url(testnet), tx_id)
            response = requests.get(url)
            try:
                raw = bytes.fromhex(response.text.strip())
            except ValueError:
                raise ValueError('unexpected response: {}'.format(response.text))
            if raw[4] == 0:
                raw = raw[:4] + raw[6:]
                tx = Tx.parse(BytesIO(raw), testnet=testnet)
                tx.locktime = little_endian_to_int(raw[-4:])
            else:
                tx = Tx.parse(BytesIO(raw), testnet=testnet)
            if tx.id() != tx_id:
                raise ValueError('not the same id: {} vs {}'.format(tx.id(), tx_id))
            cls.cache[tx_id] = tx
        cls.cache[tx_id].testnet = testnet
        return cls.cache[tx_id]