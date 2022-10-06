from shared.PrivateKey import PrivateKey
from shared.S256Point import S256Point

if __name__ == '__main__':
    print(PrivateKey(5002).public.address(False, True))
    print(PrivateKey(2020**5).public.address(True, True))
    print(PrivateKey(0x12345deadbeef).public.address(True, False))