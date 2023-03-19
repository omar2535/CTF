import random
import binascii

keybinary=random.randrange(0, pow(2,128)).to_bytes(16, byteorder='big')
print(keybinary)
