from Point import Point
from S256Field import S256Field

N = 0xfffffffffffffffffffffffffffffffebaaedce6af48a03bbfd25e8cd0364141

class S256Point(Point):
    def __init__(self, x, y, a=None, b=None):
        a = S256Field(0)
        b = S256Field(7)
        if type(x) == int:
            super().__init__(x=S256Field(x), y=S256Field(y), a=a, b=b)
        else:
            super().__init__(x=x, y=y, a=a, b=b)

    def __rmul__(self, coefficient):
        coef = coefficient % N
        return super().__rmul__(coef)

    def __repr__(self):
        if(self.x == None):
            return 'S256Point(infinity)'
        return 'S256Point({},{})'.format(hex(self.x.num), hex(self.y.num))

    def verify(self, z, sig):
        s_inv = pow(sig.s, N-2, N)
        u = z * s_inv % N
        v = sig.r * s_inv % N
        total = u*G + v*self
        return total.x.num == sig.r

G = S256Point(
    0x79be667ef9dcbbac55a06295ce870b07029bfcdb2dce28d959f2815b16f81798,
    0x483ada7726a3c4655da4fbfc0e1108a8fd17b448a68554199c47d08ffb10d4b8
    )