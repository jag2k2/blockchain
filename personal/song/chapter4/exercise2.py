from PrivateKey import PrivateKey
from S256Point import S256Point

if __name__ == '__main__':
    pub1_compressed = PrivateKey(5001).public.sec(True)
    print(pub1_compressed.hex())
    print(PrivateKey(2019**5).public.sec(True).hex())
    print(PrivateKey(0xdeadbeef54321).public.sec(True).hex())

    pub1 = S256Point.parse(pub1_compressed)
    print(pub1)
    print(PrivateKey(5001).public)

