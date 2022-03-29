import random
from binascii import unhexlify, hexlify

file = open('ciphertexts.txt', 'rb')

lines = file.readlines()

line0 = lines[0].strip().decode()
line1 = lines[1].strip().decode()
line2 = lines[2].strip().decode()
line3 = lines[3].strip().decode()

line0_unhex = unhexlify(line0)
line1_unhex = unhexlify(line1)

key_bytes = []
for i in range(0, len(line0_unhex)):
    key_bytes.append(line0_unhex[i] ^ line1_unhex[i])

print(f"key: {bytes(key_bytes)}")

plain_texts = []
for line in lines:
    line_decoded = line.strip().decode()
    line_unhex = unhexlify(line_decoded)
    plain_text = []
    for i in range(0, len(line_unhex)):
        plain_text.append(chr(line_unhex[i] ^ key_bytes[i]))
    plain_texts.append(plain_text)
    
breakpoint()
