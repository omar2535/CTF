from sympy import *
from hashlib import md5
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from random import randint, randbytes,seed
from Crypto.Util.number import bytes_to_long

for i in range(1, 92434467187580489687):
    coefficient = int(md5(i.to_bytes(32, byteorder="big")).hexdigest(),16)
    print(f"{i}\r", end="", flush=True)
    if coefficient == 93526756371754197321930622219489764824:
        print(f"Found at i={i}")
        breakpoint()