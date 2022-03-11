from pwn import *

context.log_level = 'debug'

def get_smallest(res):
    res = res.strip().decode().split(' ')
    first_num = int(res[3])
    second_num = int(res[4])
    third_num = int(res[6])
    arr = [first_num, second_num, third_num]
    return min(arr)

conn = remote('challenges.issessions.ca', '5101')

res = conn.recvline()
while 'Which is lowest?' in res.decode():
    smallest = get_smallest(res)
    conn.sendline(f"{smallest}")
    res = conn.recvline()


breakpoint()
