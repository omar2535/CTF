from pwn import *

context.log_level = 'debug'

conn = remote('challenges.issessions.ca', '5103')

res = conn.recvline()

while '+' in res.decode() or '-' in res.decode() or '/' in res.decode() or '*' in res.decode():
    math_res = eval(res.strip().decode())
    conn.sendline(str(math_res))
    res = conn.recvline()


breakpoint()
