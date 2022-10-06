from Utility import little_endian_to_int, int_to_little_endian


if __name__ == '__main__':

        h1 = bytes.fromhex('99c3980000000000')
        expected1 = 10011545
        print(little_endian_to_int(h1) == expected1)
        h2 = bytes.fromhex('a135ef0100000000')
        expected2 = 32454049
        print(little_endian_to_int(h2) == expected2)

        n1 = 1
        expected3 = b'\x01\x00\x00\x00'
        print(int_to_little_endian(n1, 4) == expected3)
        n2 = 10011545
        expected3 = b'\x99\xc3\x98\x00\x00\x00\x00\x00'
        print(int_to_little_endian(n2, 8) == expected3)