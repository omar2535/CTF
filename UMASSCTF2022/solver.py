from pwn import *

context.log_level = 'debug'


r = remote('34.148.103.218', 1228)
text = r.recvuntil('Good luck!')


text = r.recvline()
text = r.recvline()
# text = r.recvline()
# breakpoint()

# try:
#     for i in range(0, 1000):
#         print(i)
#         question = r.recvline().strip().decode()
#         r.sendline(str(eval(question)))
#         text = r.recvline()
# except Exception as e:
#     print(e)
    # breakpoint()

for i in range(0, 1000):
    print(i)
    try:
        question_raw = r.recvline()
        question_stripped = question_raw.strip()
        question = question_stripped.decode()
    except Exception as e:
        breakpoint()
    r.sendline(str(eval(question)))
    text = r.recvline()
breakpoint()


# r.recvline()