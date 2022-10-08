from shared.PrivateKey import PrivateKey
from shared.Utility import little_endian_to_int, hash256

if __name__ == '__main__':
    passphrase1 = b'jeff.tipps@utexas.edu my secret'
    secret1 = little_endian_to_int(hash256(passphrase1))
    testnet_address = PrivateKey(secret1).public.address(testnet=True)
    print(testnet_address)

    # Tx hashMessage: hash tx:b2186a8fd2adaff0172e27fe28c6bd060a5a3583a167c3563001b8d06bb4baa5

    passphrase2 = b'jeff.tipps@utexas.edu practice address'
    secret2 = little_endian_to_int(hash256(passphrase2))
    practice_address = PrivateKey(secret2).public.address(testnet=True)
    print(practice_address)

    passphrase3 = b'jeff.tipps@utexas.edu change address'
    secret3 = little_endian_to_int(hash256(passphrase3))
    change_address = PrivateKey(secret3).public.address(testnet=True)
    print(change_address)
