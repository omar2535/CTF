import random
import hashlib

# Mac/Linux: pip3 install pycryptodome
# Windows: py -m pip install pycryptodome
import Crypto.Util.number as cun
from Crypto.Cipher import AES

rand = random.SystemRandom()
FLAG = b"buckeye{???????????????????????????????????????????????????????}"
# ENTER 5 so that we can get     shared_secret = pow(B, a, p) =     A = pow(g, a, p)  # public key by setting B = g

# A
shared_secret = "492945663431124607312912596187428216236644833362983548944444265307484967310475716479559612309455174121810379737419991384759701920267928144180096029585912"
shared_secret = int(shared_secret)

# CIPHERTEXT
ciphertext_hex = "09f65b236823e2b604994aaaaddafb977ff2956416e30cef776c93fa928bac7c8901043182770656cf233fb776568de0863abb62fd5faad5ddf209a76a62b595"
ciphertext_hex = bytearray.fromhex(ciphertext_hex)
breakpoint()
# ciphertext = bytes.fromhex(ciphertext_hex)

# Use AES, a symmetric cipher, to encrypt the flag using the shared key
key = hashlib.sha1(cun.long_to_bytes(int(shared_secret))).digest()[:16]

cipher = AES.new(key, AES.MODE_ECB)
plaintext = cipher.decrypt(ciphertext_hex)
breakpoint()
# print(f"plaintext = {plaintext.decode()}")

