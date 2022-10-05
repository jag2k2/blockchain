from S256Point import S256Point, G, N
from helper import hash256

if __name__ == '__main__':
    msg_hash = int.from_bytes(hash256(b'my message'), 'big')

    private_key = int.from_bytes(hash256(b'my secret'), 'big')
    public_key = private_key*G

    # Signature Algorithm
    k = 1234567890
    k_inv = pow(k, N-2, N)
    sig_r = (k*G).x.num
    sig_s = (msg_hash + sig_r*private_key) * k_inv % N

    
    print(public_key)
    print(hex(msg_hash))
    print(hex(sig_r))
    print(hex(sig_s))

    # Signature Verification
    s_inv = pow(sig_s, N-2, N)
    u = msg_hash * s_inv % N
    v = sig_r * s_inv % N
    
    print((u*G + v*public_key).x.num == sig_r)