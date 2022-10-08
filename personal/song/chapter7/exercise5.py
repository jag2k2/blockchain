from shared.Tx import SIGHASH_ALL, Tx, TxIn, TxOut
from shared.Utility import decode_base58, little_endian_to_int, hash256
from shared.Script import Script
from shared.PrivateKey import PrivateKey

if __name__ == '__main__':
    passphrase2 = b'jeff.tipps@utexas.edu practice address'
    secret2 = little_endian_to_int(hash256(passphrase2))
    private_key2 = PrivateKey(secret2)
    practice_address = private_key2.public_key.address(testnet=True)
    print(practice_address + ": " + decode_base58(practice_address).hex()) # miTVw9CvEPnQ4Z4ZTTFQ1jm4X47PqYghgB

    passphrase3 = b'jeff.tipps@utexas.edu change address'
    secret3 = little_endian_to_int(hash256(passphrase3))
    private_key3 = PrivateKey(secret3)
    change_address = private_key3.public_key.address(testnet=True)
    print(change_address + ": " + decode_base58(change_address).hex()) # mpd4shwkfpDyNiNgDAm4G6u1jZiiT6F8iU
    
    passphrase4 = b'jeff.tipps@utexas.edu final address'
    secret4 = little_endian_to_int(hash256(passphrase4))
    private_key4 = PrivateKey(secret4)
    final_address = private_key4.public_key.address(testnet=True)
    print(final_address + ": " + decode_base58(final_address).hex()) # msKh9SnDd4UQVBajk55FdPWqunounRy5E8

    sats = 30000
    funding_tx_from_testnet = '68ac91b864a2e833e8acb272db0be68e5bde52d346366a94762eb38350a83eba'
    prev_tx = bytes.fromhex(funding_tx_from_testnet)
    prev_index = 0
    tx_in1 = TxIn(prev_tx, prev_index)

    sats = 15000
    funding_tx_from_testnet = '68ac91b864a2e833e8acb272db0be68e5bde52d346366a94762eb38350a83eba'
    prev_tx = bytes.fromhex(funding_tx_from_testnet)
    prev_index = 1
    tx_in2 = TxIn(prev_tx, prev_index)

    target_amount = 40000
    target_h160 = decode_base58('msKh9SnDd4UQVBajk55FdPWqunounRy5E8')
    target_script = Script.p2pkh_script(target_h160)
    target_output = TxOut(target_amount, target_script)

    tx_obj = Tx(1, [tx_in1, tx_in2], [target_output], 0, True)
   
    print(tx_obj)

    z = tx_obj.sig_hash(0)
    tx_obj.sign_input(0, private_key2)
    tx_obj.sign_input(1, private_key3)
    
    print(tx_obj)
    print("tx_id: " + tx_obj.id())
    print(tx_obj.serialize().hex())

    # tx_id: 68ac91b864a2e833e8acb272db0be68e5bde52d346366a94762eb38350a83eba