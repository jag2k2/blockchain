from Point import Point
from FieldElement import FieldElement
from S256Point import G, N

if __name__ == '__main__':
    a = 0
    b = 7

    gx = 0x79be667ef9dcbbac55a06295ce870b07029bfcdb2dce28d959f2815b16f81798
    gy = 0x483ada7726a3c4655da4fbfc0e1108a8fd17b448a68554199c47d08ffb10d4b8
    n = 0xfffffffffffffffffffffffffffffffebaaedce6af48a03bbfd25e8cd0364141

    p = 2**256 - 2 **32 - 977

    x = FieldElement(gx,p)
    y = FieldElement(gy,p)
    a = FieldElement(0,p)
    b = FieldElement(7,p)

    G1 = Point(x, y, a, b);
    print (G1);
    print (n*G1)

    print(G)
    print(N*G)