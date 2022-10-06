from random import randint
from S256Point import G, N
from Signature import Signature

import hashlib
import hmac

class PrivateKey:
    def __init__(self, secret):
        self.secret = secret
        self.public = secret * G

    def hex(self):
        return '{:x}'.format(self.secret).zfill(64)

    def sign(self, msg_hash):
        k = self.deterministic_k(z)
        k_inv = pow(k, N-2, N)
        r =(k*G).x.num
        s = (msg_hash + r*self.secret) * k_inv % N
        if s > N/2:
            s = N - s
        return Signature(r,s)

    def deterministic_k(self, z):
        k = b'\x00' * 32
        v = b'\x01' * 32
        if z > N:
            z -= N
        z_bytes = z.to_bytes(32, 'big')
        secret_bytes = self.secret.to_bytes(32, 'big')
        s256 = hashlib.sha256
        k = hmac.new(k, v + b'\x00' + secret_bytes + z_bytes, s256).digest()
        v = hmac.new(k, v, s256).digest()
        k = hmac.new(k, v + b'\x01' + secret_bytes + z_bytes, s256).digest()
        v = hmac.new(k, v, s256).digest()
        while True:
            v = hmac.new(k, v, s256).digest()
            candidate = int.from_bytes(v, 'big')
            if candidate >= 1 and candidate < N:
                return candidate  # <2>
            k = hmac.new(k, v + b'\x00', s256).digest()
            v = hmac.new(k, v, s256).digest()
