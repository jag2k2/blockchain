from shared.Tx import SIGHASH_ALL, Tx, TxIn, TxOut
from shared.Utility import decode_base58
from shared.Script import Script
from shared.PrivateKey import PrivateKey

if __name__ == '__main__':
    prev_tx = bytes.fromhex('0d6fe5213c0b3291f208cba8bfb59b7476dffacc4e5cb66f6eb20a080843a299')
    prev_index = 13
    tx_in = TxIn(prev_tx, prev_index)
    
    change_amount = int(0.33 * 100000000)  # number of satoshi
    change_h160 = decode_base58('mzx5YhAH9kNHtcN481u6WkjeHjYtVeKVh2')
    change_script = Script.p2pkh_script(change_h160)
    change_output = TxOut(change_amount, change_script)
    
    target_amount = int(0.1 * 100000000)
    target_h160 = decode_base58('mnrVtF8DWjMu839VW3rBfgYaAfKk8983Xf')
    target_script = Script.p2pkh_script(target_h160)
    target_output = TxOut(target_amount, target_script)

    tx_obj = Tx(1, [tx_in], [change_output, target_output], 0, True)
    print(tx_obj)           #  We have created a transaction but the ScriptSigs of every input are currently blank.  This transaction needs to be signed!

    # To sign, we need 2 things.  
    # (1) The public key that hashes to utxo ScriptPubKey h160
    # (2) z, which is the hash of the modified transaction (which we did in the last section)

    z = tx_obj.sig_hash(0)
    print(z)
    private_key = PrivateKey(secret=8675309)
    sig = private_key.sign(z)                   # create the signature
    der = sig.der()
    sig = der + SIGHASH_ALL.to_bytes(1, 'big')
    sec = private_key.public_key.sec()
    script_sig = Script([sig, sec])             # create the signature script
    tx_obj.tx_ins[0].script_sig = script_sig    # sign the transaction's input
    print(tx_obj)

