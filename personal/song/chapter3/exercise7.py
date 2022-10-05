from S256Point import S256Point, G, N
from helper import hash256

if __name__ == '__main__':
    private_key = 12345
    msg_hash = int.from_bytes(hash256(b'Programming Bitcoin!'), 'big')
    k = 1234567890
    r = (k*G).x.num
    k_inv = pow(k, N-2, N)
    s = (msg_hash + r*e) * k_inv % N
    public_key = private_key*G
    
    print(public_key)
    print(hex(msg_hash))
    print(hex(r))
    print(hex(s))