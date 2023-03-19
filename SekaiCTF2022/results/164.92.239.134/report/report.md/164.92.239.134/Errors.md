```
[*] Port scan Top TCP Ports (top-tcp-ports) ran a command which returned a non-zero exit code (139).
[-] Command: nmap -vv --reason -Pn -T4 -sV -sC --version-all -A --osscan-guess -oN "/home/omar2535/Desktop/programming/CTF/SekaiCTF2022/results/164.92.239.134/scans/_quick_tcp_nmap.txt" -oX "/home/omar2535/Desktop/programming/CTF/SekaiCTF2022/results/164.92.239.134/scans/xml/_quick_tcp_nmap.xml" 164.92.239.134
[-] Error Output:
Host discovery disabled (-Pn). All addresses will be marked 'up' and scan times may be slower.
Segmentation fault


[*] Port scan All TCP Ports (all-tcp-ports) ran a command which returned a non-zero exit code (139).
[-] Command: nmap -vv --reason -Pn -T4 -sV -sC --version-all -A --osscan-guess -p- -oN "/home/omar2535/Desktop/programming/CTF/SekaiCTF2022/results/164.92.239.134/scans/_full_tcp_nmap.txt" -oX "/home/omar2535/Desktop/programming/CTF/SekaiCTF2022/results/164.92.239.134/scans/xml/_full_tcp_nmap.xml" 164.92.239.134
[-] Error Output:
Host discovery disabled (-Pn). All addresses will be marked 'up' and scan times may be slower.
Segmentation fault


[*] Service scan Nmap SSH (tcp/22/ssh/nmap-ssh) ran a command which returned a non-zero exit code (139).
[-] Command: nmap -vv --reason -Pn -T4 -sV -p 22 --script="banner,ssh2-enum-algos,ssh-hostkey,ssh-auth-methods" -oN "/home/omar2535/Desktop/programming/CTF/SekaiCTF2022/results/164.92.239.134/scans/tcp22/tcp_22_ssh_nmap.txt" -oX "/home/omar2535/Desktop/programming/CTF/SekaiCTF2022/results/164.92.239.134/scans/tcp22/xml/tcp_22_ssh_nmap.xml" 164.92.239.134
[-] Error Output:
Host discovery disabled (-Pn). All addresses will be marked 'up' and scan times may be slower.
Segmentation fault


[*] Service scan Nmap HTTP (tcp/80/http/nmap-http) ran a command which returned a non-zero exit code (139).
[-] Command: nmap -vv --reason -Pn -T4 -sV -p 80 --script="banner,(http* or ssl*) and not (brute or broadcast or dos or external or http-slowloris* or fuzzer)" -oN "/home/omar2535/Desktop/programming/CTF/SekaiCTF2022/results/164.92.239.134/scans/tcp80/tcp_80_http_nmap.txt" -oX "/home/omar2535/Desktop/programming/CTF/SekaiCTF2022/results/164.92.239.134/scans/tcp80/xml/tcp_80_http_nmap.xml" 164.92.239.134
[-] Error Output:
Host discovery disabled (-Pn). All addresses will be marked 'up' and scan times may be slower.
Bug in http-security-headers: no string output.
Segmentation fault



```