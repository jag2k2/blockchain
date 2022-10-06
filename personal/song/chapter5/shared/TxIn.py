from shared.Utility import little_endian_to_int, read_varint

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
        return '{}:{}'.format(self.prev_tex.hex(), self.prev_index)

    @classmethod
    def parse(self, stream):
        prev_tx_id = stream.read(32)[::-1]
        prev_tx_index = little_endian_to_int(stream.read(4))
        script_sig = Script.parse(stream)
        sequence = little_endian_to_int(stream.read(4))
        return self(prev_tx_id, prev_tx_index, script_sig, sequence)