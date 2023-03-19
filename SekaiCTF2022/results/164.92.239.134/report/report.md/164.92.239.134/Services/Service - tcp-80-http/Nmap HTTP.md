```bash
nmap -vv --reason -Pn -T4 -sV -p 80 --script="banner,(http* or ssl*) and not (brute or broadcast or dos or external or http-slowloris* or fuzzer)" -oN "/home/omar2535/Desktop/programming/CTF/SekaiCTF2022/results/164.92.239.134/scans/tcp80/tcp_80_http_nmap.txt" -oX "/home/omar2535/Desktop/programming/CTF/SekaiCTF2022/results/164.92.239.134/scans/tcp80/xml/tcp_80_http_nmap.xml" 164.92.239.134
```

[/home/omar2535/Desktop/programming/CTF/SekaiCTF2022/results/164.92.239.134/scans/tcp80/tcp_80_http_nmap.txt](file:///home/omar2535/Desktop/programming/CTF/SekaiCTF2022/results/164.92.239.134/scans/tcp80/tcp_80_http_nmap.txt):

```
# Nmap 7.92 scan initiated Fri Sep 30 16:03:44 2022 as: nmap -vv --reason -Pn -T4 -sV -p 80 "--script=banner,(http* or ssl*) and not (brute or broadcast or dos or external or http-slowloris* or fuzzer)" -oN /home/omar2535/Desktop/programming/CTF/SekaiCTF2022/results/164.92.239.134/scans/tcp80/tcp_80_http_nmap.txt -oX /home/omar2535/Desktop/programming/CTF/SekaiCTF2022/results/164.92.239.134/scans/tcp80/xml/tcp_80_http_nmap.xml 164.92.239.134
Nmap scan report for 164.92.239.134
Host is up, received user-set (0.16s latency).
Scanned at 2022-09-30 16:03:44 PDT for 35s

Bug in http-security-headers: no string output.
PORT   STATE SERVICE REASON  VERSION
80/tcp open  http    syn-ack Apache httpd 2.4.41 ((Ubuntu))
|_http-jsonp-detection: Couldn't find any JSONP endpoints.
|_http-mobileversion-checker: No mobile version detected.
|_http-referer-checker: Couldn't find any cross-domain scripts.
|_http-wordpress-enum: Nothing found amongst the top 100 resources,use --script-args search-limit=<number|all> for deeper analysis)
| http-vhosts: 
|_128 names had status 200
|_http-feed: Couldn't find any feeds.
|_http-drupal-enum: Nothing found amongst the top 100 resources,use --script-args number=<number|all> for deeper analysis)
|_http-malware-host: Host appears to be clean
|_http-fetch: Please enter the complete path of the directory to save data in.
| http-sitemap-generator: 
|   Directory structure:
|     /
|       Other: 1; css: 1; js: 1
|   Longest directory structure:
|     Depth: 0
|     Dir: /
|   Total files found (by extension):
|_    Other: 1; css: 1; js: 1
|_http-errors: Couldn't find any error pages.
| http-useragent-tester: 
|   Status for browser useragent: 200
|   Allowed User Agents: 
|     Mozilla/5.0 (compatible; Nmap Scripting Engine; https://nmap.org/book/nse.html)
|     libwww
|     lwp-trivial
|     libcurl-agent/1.0
|     PHP/
|     Python-urllib/2.5
|     GT::WWW
|     Snoopy
|     MFC_Tear_Sample
|     HTTP::Lite
|     PHPCrawl
|     URI::Fetch
|     Zend_Http_Client
|     http client
|     PECL::HTTP
|     Wget/1.13.4 (linux-gnu)
|_    WWW-Mechanize/1.34
|_http-chrono: Request times for /; avg: 415.54ms; min: 382.45ms; max: 467.89ms
| http-comments-displayer: 
| Spidering limited to: maxdepth=3; maxpagecount=20; withinhost=164.92.239.134
|     
|     Path: http://164.92.239.134:80/style.css
|     Line number: 110
|     Comment: 
|         /**
|          * Flex Grid
|          */
|     
|     Path: http://164.92.239.134:80/style.css
|     Line number: 87
|     Comment: 
|         /**
|          * Text Selection
|          */
|     
|     Path: http://164.92.239.134:80/style.css
|     Line number: 113
|     Comment: 
|         /**
|          * Box Shadow
|          */
|     
|     Path: http://164.92.239.134:80/style.css
|     Line number: 495
|     Comment: 
|         /**
|          * Color Helpers
|          */
|     
|     Path: http://164.92.239.134:80/style.css
|     Line number: 4
|     Comment: 
|         /**
|          * Base Settings/Overwrite Normalize
|          */
|     
|     Path: http://164.92.239.134:80/style.css
|     Line number: 116
|     Comment: 
|         /**
|          * Letter Spacing
|          */
|     
|     Path: http://164.92.239.134:80/style.css
|     Line number: 139
|     Comment: 
|         /**
|          * Body
|          */
|     
|     Path: http://164.92.239.134:80/
|     Line number: 12
|     Comment: 
|         <!-- partial:index.partial.html -->
|     
|     Path: http://164.92.239.134:80/style.css
|     Line number: 146
|     Comment: 
|         /**
|          * Sections
|          */
|     
|     Path: http://164.92.239.134:80/style.css
|     Line number: 481
|     Comment: 
|         /**
|          * Absolute Background Cover
|          */
|     
|     Path: http://164.92.239.134:80/
|     Line number: 148
|     Comment: 
|         <!-- partial -->
|     
|     Path: http://164.92.239.134:80/style.css
|     Line number: 171
|     Comment: 
|         /**
|          * Blog page
|          */
|     
|     Path: http://164.92.239.134:80/style.css
|     Line number: 125
|     Comment: 
|         /**
|          * Black Color Overlay
|          */
|     
|     Path: http://164.92.239.134:80/style.css
|     Line number: 203
|     Comment: 
|         /**
|          * Tabs
|          * On the Blog page for posts and categories
|          */
|     
|     Path: http://164.92.239.134:80/style.css
|     Line number: 411
|     Comment: 
|         /**
|          * Footer
|          */
|     
|     Path: http://164.92.239.134:80/style.css
|     Line number: 1
|     Comment: 
|         /**
|          * Base Variables
|          */
|     
|     Path: http://164.92.239.134:80/style.css
|     Line number: 325
|     Comment: 
|         /**
|          * Category Card
|          * On the blog page under category tab
|          */
|     
|     Path: http://164.92.239.134:80/style.css
|     Line number: 253
|     Comment: 
|         /**
|          * Blog Post Preview
|          * On the Blog page
|          */
|     
|     Path: http://164.92.239.134:80/style.css
|     Line number: 101
|     Comment: 
|         /**
|          * Underline Slide from left and back
|          */
|     
|     Path: http://164.92.239.134:80/style.css
|     Line number: 456
|     Comment: 
|         /**
|          * Animations
|          */
|     
|     Path: http://164.92.239.134:80/style.css
|     Line number: 163
|     Comment: 
|         /**
|          * Class Container (BEM)
|          */
|     
|     Path: http://164.92.239.134:80/style.css
|     Line number: 104
|     Comment: 
|         /**
|          * Button Slide
|          * Need to still add hover state in parent element
|          * box-shadow: inset 175px 0 0 0 $color-alpha;
|          * color: $color-white;
|_         */
| http-php-version: Logo query returned unknown hash 39207259befdf69b8617aa2df7e8a354
|_Credits query returned unknown hash 39207259befdf69b8617aa2df7e8a354
|_http-server-header: Apache/2.4.41 (Ubuntu)
|_http-stored-xss: Couldn't find any stored XSS vulnerabilities.
| http-methods: 
|_  Supported Methods: GET POST OPTIONS HEAD
|_http-csrf: Couldn't find any CSRF vulnerabilities.
|_http-date: Fri, 30 Sep 2022 23:03:57 GMT; 0s from local time.
|_http-dombased-xss: Couldn't find any DOM based XSS.
|_http-config-backup: ERROR: Script execution failed (use -d to debug)
|_http-wordpress-users: [Error] Wordpress installation was not found. We couldn't find wp-login.php
| http-headers: 
|   Date: Fri, 30 Sep 2022 23:03:54 GMT
|   Server: Apache/2.4.41 (Ubuntu)
|   Last-Modified: Sun, 28 Aug 2022 08:31:28 GMT
|   ETag: "1d48-5e748f931b800"
|   Accept-Ranges: bytes
|   Content-Length: 7496
|   Vary: Accept-Encoding
|   Connection: close
|   Content-Type: text/html
|   
|_  (Request type: HEAD)
|_http-litespeed-sourcecode-download: Request with null byte did not work. This web server might not be vulnerable
|_http-devframework: Couldn't determine the underlying framework or CMS. Try increasing 'httpspider.maxpagecount' value to spider more pages.
|_http-title: Sekai Blog

Read data files from: /usr/bin/../share/nmap
Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
# Nmap done at Fri Sep 30 16:04:19 2022 -- 1 IP address (1 host up) scanned in 34.57 seconds

```
