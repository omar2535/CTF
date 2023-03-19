import os
import subprocess


for i in range(0, 10000):
    output = subprocess.check_output(['php', '-r', f"echo hash('tiger160,4', {i}, false);"])
    if output.decode()[0:2] == '0e':
        breakpoint()

    