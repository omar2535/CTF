from sympy import *
from hashlib import md5
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from random import randint, randbytes,seed
from Crypto.Util.number import bytes_to_long
from binascii import unhexlify

dummyflag = "lol"
FLAG = b'HTB{dummyflag}'
flag_enc = b'1aaad05f3f187bcbb3fb5c9e233ea339082062fc10a59604d96bcc38d0af92cd842ad7301b5b72bd5378265dae0bc1c1e9f09a90c97b35cfadbcfe259021ce495e9b91d29f563ae7d49b66296f15e7999c9e547fac6f1a2ee682579143da511475ea791d24b5df6affb33147d57718eaa5b1b578230d97f395c458fc2c9c36525db1ba7b1097ad8f5df079994b383b32695ed9a372ea9a0eb1c6c18b3d3d43bd2db598667ef4f80845424d6c75abc88b59ef7c119d505cd696ed01c65f374a0df3f331d7347052faab63f76f587400b6a6f8b718df1db9cebe46a4ec6529bc226627d39baca7716a4c11be6f884c371b08d87c9e432af58c030382b737b9bb63045268a18455b9f1c4011a984a818a5427231320ee7eca39bdfe175333341b7c'
class Shamir:
    def __init__(self, prime, k, n):
        self.p = prime
        self.secret = 15 # randint(1,self.p-1)
        self.k = k
        self.n = n
        self.coeffs = [self.secret]
        self.x_vals = []
        self.y_vals = []

    def next_coeff(self, val):
        # breakpoint()
        return int(md5(val.to_bytes(32, byteorder="big")).hexdigest(),16)

    def calc_coeffs(self):
        for i in range(1, self.n + 1):
            self.coeffs.append(self.next_coeff(self.coeffs[i-1]))

    def calc_y(self, x):
        y = 0
        for i, coeff in enumerate(self.coeffs):        
            y += coeff * x**i
        return y % self.p


    def create_pol(self):
        self.calc_coeffs()
        self.coeffs = self.coeffs[:self.k]
        for i in range(self.n):
            x = randint(1,self.p-1)
            self.x_vals.append(x)
            self.y_vals.append(self.calc_y(x))

    def get_share(self):
        return self.x_vals[0], self.y_vals[0]


def main():
    sss = Shamir(92434467187580489687, 10, 18)
    sss.create_pol()
    share = sss.get_share()
    secret = 39612257993477957104
    seed(secret)
    key = randbytes(16)
    cipher = AES.new(key, AES.MODE_ECB)
    enc_FLAG = cipher.encrypt(pad(FLAG,16)).hex()
    res = cipher.decrypt(unhexlify(flag_enc))
    
    breakpoint()
    # f = open('new_msg.enc', 'w')
    # f.write('share: ' + str(share) + '\n')
    # f.write('coefficient: ' + str(sss.coeffs[1]) + '\n')
    # f.write('secret message: ' + str(enc_FLAG) + '\n')
    # f.close()

    print('share: ' + str(share))
    print('coefficient: ' + str(sss.coeffs[1]))
    print('secret message: ' + str(enc_FLAG))
    
if __name__ == "__main__":
    main()


