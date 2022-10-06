from shared.PrivateKey import PrivateKey
from chapter5.shared.Tx import Tx

if __name__ == '__main__':
    transaction1 = Tx(1, None, None, None, testnet=False)
    print(transaction1)