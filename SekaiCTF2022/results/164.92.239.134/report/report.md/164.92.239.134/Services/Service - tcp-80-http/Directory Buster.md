```bash
feroxbuster -u http://164.92.239.134:80/ -t 10 -w /home/omar2535/.config/AutoRecon/wordlists/dirbuster.txt -x "txt,html,php,asp,aspx,jsp" -v -k -n -q -e -o "/home/omar2535/Desktop/programming/CTF/SekaiCTF2022/results/164.92.239.134/scans/tcp80/tcp_80_http_feroxbuster_dirbuster.txt"
```

[/home/omar2535/Desktop/programming/CTF/SekaiCTF2022/results/164.92.239.134/scans/tcp80/tcp_80_http_feroxbuster_dirbuster.txt](file:///home/omar2535/Desktop/programming/CTF/SekaiCTF2022/results/164.92.239.134/scans/tcp80/tcp_80_http_feroxbuster_dirbuster.txt):

```
200      GET      504l     1050w     7863c http://164.92.239.134/style.css
200      GET      102l      196w     2496c http://164.92.239.134/script.js
200      GET      152l      410w     7496c http://164.92.239.134/
403      GET        9l       28w      279c http://164.92.239.134/.html
403      GET        9l       28w      279c http://164.92.239.134/.hta
403      GET        9l       28w      279c http://164.92.239.134/.htaccess
403      GET        9l       28w      279c http://164.92.239.134/.htpasswd
403      GET        9l       28w      279c http://164.92.239.134/.hta.txt
403      GET        9l       28w      279c http://164.92.239.134/.htaccess.txt
403      GET        9l       28w      279c http://164.92.239.134/.htpasswd.txt
403      GET        9l       28w      279c http://164.92.239.134/.hta.html
403      GET        9l       28w      279c http://164.92.239.134/.htaccess.html
403      GET        9l       28w      279c http://164.92.239.134/.htpasswd.html
403      GET        9l       28w      279c http://164.92.239.134/.hta.php
403      GET        9l       28w      279c http://164.92.239.134/.htaccess.php
403      GET        9l       28w      279c http://164.92.239.134/.htpasswd.php
403      GET        9l       28w      279c http://164.92.239.134/.hta.asp
403      GET        9l       28w      279c http://164.92.239.134/.htaccess.asp
403      GET        9l       28w      279c http://164.92.239.134/.htpasswd.asp
403      GET        9l       28w      279c http://164.92.239.134/.hta.aspx
403      GET        9l       28w      279c http://164.92.239.134/.htaccess.aspx
403      GET        9l       28w      279c http://164.92.239.134/.htpasswd.aspx
403      GET        9l       28w      279c http://164.92.239.134/.hta.jsp
403      GET        9l       28w      279c http://164.92.239.134/.htaccess.jsp
403      GET        9l       28w      279c http://164.92.239.134/.htpasswd.jsp
200      GET      152l      410w     7496c http://164.92.239.134/index.html
403      GET        9l       28w      279c http://164.92.239.134/server-status

```