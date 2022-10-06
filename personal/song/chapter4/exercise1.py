from PrivateKey import PrivateKey

if __name__ == '__main__':
    print(PrivateKey(5000).public.sec(False).hex())
    print(PrivateKey(2018**5).public.sec(False).hex())
    print(PrivateKey(0xdeadbeef12345).public.sec(False).hex())