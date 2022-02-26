from pwn import *

vaults = ['vault1.momandpopsflags.ca', 'vault2.momandpopsflags.ca', 'vault3.momandpopsflags.ca']

r = remote(vaults[2], 5555)
res = r.recvline()

r.sendline(b'INITIALIZE CONNECTION')
res = r.recvline()

r.sendline(b'SEND FLAG')
res = r.recvline()
challenge_string = res.strip().decode().split(' ')[-1]

r.sendline(challenge_string.encode('utf-8'))
res = r.recvall()
print(res.decode())
