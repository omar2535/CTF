```bash
whatweb --color=never --no-errors -a 3 -v http://164.92.239.134:80 2>&1
```

[/home/omar2535/Desktop/programming/CTF/SekaiCTF2022/results/164.92.239.134/scans/tcp80/tcp_80_http_whatweb.txt](file:///home/omar2535/Desktop/programming/CTF/SekaiCTF2022/results/164.92.239.134/scans/tcp80/tcp_80_http_whatweb.txt):

```
WhatWeb report for http://164.92.239.134:80
Status    : 200 OK
Title     : Sekai Blog
IP        : 164.92.239.134
Country   : UNITED STATES, US

Summary   : Apache[2.4.41], HTML5, HTTPServer[Ubuntu Linux][Apache/2.4.41 (Ubuntu)], Script

Detected Plugins:
[ Apache ]
	The Apache HTTP Server Project is an effort to develop and
	maintain an open-source HTTP server for modern operating
	systems including UNIX and Windows NT. The goal of this
	project is to provide a secure, efficient and extensible
	server that provides HTTP services in sync with the current
	HTTP standards.

	Version      : 2.4.41 (from HTTP Server Header)
	Google Dorks: (3)
	Website     : http://httpd.apache.org/

[ HTML5 ]
	HTML version 5, detected by the doctype declaration


[ HTTPServer ]
	HTTP server header string. This plugin also attempts to
	identify the operating system from the server header.

	OS           : Ubuntu Linux
	String       : Apache/2.4.41 (Ubuntu) (from server string)

[ Script ]
	This plugin detects instances of script HTML elements and
	returns the script language/type.


HTTP Headers:
	HTTP/1.1 200 OK
	Date: Fri, 30 Sep 2022 23:03:46 GMT
	Server: Apache/2.4.41 (Ubuntu)
	Last-Modified: Sun, 28 Aug 2022 08:31:28 GMT
	ETag: "1d48-5e748f931b800-gzip"
	Accept-Ranges: bytes
	Vary: Accept-Encoding
	Content-Encoding: gzip
	Content-Length: 1296
	Connection: close
	Content-Type: text/html



```
