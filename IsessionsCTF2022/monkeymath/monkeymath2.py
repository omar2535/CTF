from pwn import *

context.log_level = 'debug'

def sanitize(res):
    new_res = res.strip().decode().split(' ')
    sanitized = []
    for i in range(0, len(new_res)):
        if i % 2 != 0:
            sanitized.append(new_res[i][0])
        else:
            sanitized.append(new_res[i])
    return ''.join(sanitized)
        

conn = remote('challenges.issessions.ca', '5104')

res = conn.recvline()

while '+' in res.decode() or '-' in res.decode() or '/' in res.decode() or '*' in res.decode():
    sanitized = sanitize(res)
    # breakpoint()
    math_res = eval(sanitized)
    conn.sendline(str(math_res))
    res = conn.recvline()
    res = conn.recvline()
    


breakpoint()
