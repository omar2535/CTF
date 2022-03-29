def shift(c):
    n = ord(c)
    if c >= '0' and c <= '9':
        n = n - ord('0')
        n = (n + 9) % 10
        return chr(n + ord('0'))
    elif c >= 'a' and c <= 'z':
        n = n - ord('a')
        n = (n + 25) % 26
        return chr(n + ord('a'))
    elif c >= 'A' and c <= 'Z':
        n = n - ord('A')
        n = (n + 25) % 26
        return chr(n + ord('A'))
    elif c == '*':
        return '{'
    elif c == '^':
        return '}'
    elif c == '#':
        return '_'
    
flag = "npolfzDUG*Fyus5dujoh#GUQ^"

plain = ""

for c in flag:
    plain += shift(c)

print('flag: {}'.format(plain))
