```bash
nmap -vv --reason -Pn -T4 -sV -sC --version-all -A --osscan-guess -oN "/home/omar2535/Desktop/programming/CTF/SekaiCTF2022/results/164.92.239.134/scans/_quick_tcp_nmap.txt" -oX "/home/omar2535/Desktop/programming/CTF/SekaiCTF2022/results/164.92.239.134/scans/xml/_quick_tcp_nmap.xml" 164.92.239.134
```

[/home/omar2535/Desktop/programming/CTF/SekaiCTF2022/results/164.92.239.134/scans/_quick_tcp_nmap.txt](file:///home/omar2535/Desktop/programming/CTF/SekaiCTF2022/results/164.92.239.134/scans/_quick_tcp_nmap.txt):

```
# Nmap 7.92 scan initiated Fri Sep 30 16:00:38 2022 as: nmap -vv --reason -Pn -T4 -sV -sC --version-all -A --osscan-guess -oN /home/omar2535/Desktop/programming/CTF/SekaiCTF2022/results/164.92.239.134/scans/_quick_tcp_nmap.txt -oX /home/omar2535/Desktop/programming/CTF/SekaiCTF2022/results/164.92.239.134/scans/xml/_quick_tcp_nmap.xml 164.92.239.134
Nmap scan report for 164.92.239.134
Host is up, received user-set (0.15s latency).
Scanned at 2022-09-30 16:00:39 PDT for 32s
Not shown: 998 filtered tcp ports (no-response)
PORT   STATE SERVICE    REASON  VERSION
22/tcp open  tcpwrapped syn-ack
| ssh-hostkey: 
|   3072 70:01:39:b5:bd:6e:7a:3d:42:be:f1:84:ec:3a:15:f3 (RSA)
| ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABgQDTJ0zGKrT4zpnYABmgzm58MH9da3fVsQxZ0/4rsG4h8qDVxwjpSBtBsom0QEj3Jplb+/kcqmEd4fubeyLjDtQmORxdJCQlvMcwSXc2Oqwfd5D9Gjt2jZoLY0f8mdvq87B3AobsxGzkcTzgrtQSRCXZYpisGw24QXj/NWRjeTJpwi9HyAhu7APjrwuUQdDV1wzj4qp4mkAd/UVDuhf6XKJK7+5Mxk3ZnltPi4Fy7Ur4xJhyoBdBi0f4AlGsyOZeQiuJhpAyTvsPM6v4gOZrpUEUN6Ts9/gIKK0aoYCHrCUO5bnc/TRy5diAA+zMGnT/KvhUtfeUENyBRB9AZQ8XlfwR38kISQDAR4M9NpYyxB/9ObUuT4/Vw/FYLLg+686cR5dggBfsXBstBdn+rDIywARL3kNqHbYSNkR23c/KOs0aSnxr+sAEt3AOouJQX/mITP68FgAWH31MEpznMVXzc0wIODrGptpyRvm5OtNS7CD9oZWOFl09njtVjaXCwd6Bxlk=
|   256 5f:22:fa:f2:cd:8a:66:f1:b7:f6:f7:40:4c:6b:78:52 (ECDSA)
| ecdsa-sha2-nistp256 AAAAE2VjZHNhLXNoYTItbmlzdHAyNTYAAAAIbmlzdHAyNTYAAABBBOsoZjRYIfBfkcQRwZYjbfHpuLfZxn0ydzAqMKYXkUK1/r+HqHa8SP5PFM0+7gantRuN4xARmwTexhOhq27llYU=
|   256 83:83:7b:73:d4:9c:85:04:1b:2a:a0:c9:76:55:4b:67 (ED25519)
|_ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIAy7qfiCdiDEd4CdzAcWGqUepaS9sj4RNeeTA3a1dDJ+
80/tcp open  tcpwrapped syn-ack
|_http-title: Sekai Blog
| http-methods: 
|_  Supported Methods: GET POST OPTIONS HEAD
|_http-server-header: Apache/2.4.41 (Ubuntu)

Read data files from: /usr/bin/../share/nmap
Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
# Nmap done at Fri Sep 30 16:01:11 2022 -- 1 IP address (1 host up) scanned in 32.38 seconds

```
