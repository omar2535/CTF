import os
import subprocess

payload = "A"

for i in range(0, 3000):
    payload = payload * i
    result = os.system(f"echo {payload} | ./timeserver")
    breakpoint()