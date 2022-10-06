from shared.Utility import encode_base58

if __name__ == '__main__':
    hex1 = '7c076ff316692a3d7eb3c3bb0f8b1488cf72e1afcd929e29307032997a838a3d'
    hex2 = 'eff69ef2b1bd93a66ed5219add4fb51e11a840f404876325a1e8ffe0529a2c'
    hex3 = 'c7207fee197d27c618aea621406f6bf5ef6fca38681d82b2f06fddbdce6feab6'

    print(encode_base58(bytes.fromhex(hex1)))
    print(encode_base58(bytes.fromhex(hex2)))
    print(encode_base58(bytes.fromhex(hex3)))