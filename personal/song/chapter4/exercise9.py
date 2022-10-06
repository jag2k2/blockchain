from shared.PrivateKey import PrivateKey
from shared.Utility import little_endian_to_int, hash256

if __name__ == '__main__':
    passphrase1 = b'jeff.tipps@utexas.edu my secret'
    passphrase2 = b'jimmy@programmingblockchain.com my secret'
    secret = little_endian_to_int(hash256(passphrase1))
    print(PrivateKey(secret).public.address(testnet=True))

    # Tx hashMessage: hash tx:b2186a8fd2adaff0172e27fe28c6bd060a5a3583a167c3563001b8d06bb4baa5