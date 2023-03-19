import nclib
import base64
import codecs
from urllib.parse import unquote

def get_param(response):
    return response.decode('utf-8').split(':')[1].strip()

nc = nclib.Netcat(('34.87.231.237', 31905), verbose=True)

# Initial connection
response = nc.recv()
print(response)

# Send the enter
nc.send(b'\n')
response = nc.recv()

# 1+1=? 2
nc.send(b'2\n')
response = nc.recv()

"""Decode this hex string and provide me the original number (base 10):"""
hex_str = get_param(response)
dec_str = int(hex_str, 16)
# print(f"Hex string: {hex_str}, decimal: {dec_str}")
nc.send(f"{dec_str}\n")
response = nc.recv()


"""Decode this hex string and provide me the original ASCII letter:"""
hex_str = get_param(response)
ascii_str = bytes.fromhex(hex_str).decode('ASCII')
nc.send(f"{ascii_str}\n")
response = nc.recv()

"""Decode this URL encoded string and provide me the original ASCII symbols:"""
url_encoded_str = get_param(response)
url_decoded_str = unquote(url_encoded_str)
nc.send(f"{url_decoded_str}\n")
response = nc.recv()

"""Decode this base64 string and provide me the plaintext:"""
b64_text_encoded = get_param(response)
b64_text_decoded = base64.b64decode(b64_text_encoded).decode('utf-8')
nc.send(f"{b64_text_decoded}\n")
response = nc.recv()

"""Encode this plaintext string and provide me the Base64:"""
b64_text_decoded = get_param(response)
b64_text_encoded = base64.b64encode(b64_text_decoded.encode('utf-8')).decode('utf-8')
nc.send(f"{b64_text_encoded}\n")
response = nc.recv()

"""Decode this rot13 string and provide me the plaintext:"""
rot_13_encoded = get_param(response)
rot_13_decoded = codecs.decode(rot_13_encoded, 'rot_13')
nc.send(f"{rot_13_decoded}\n")
response = nc.recv()

"""Encode this plaintext string and provide me the ROT13 equilavent:"""
rot_13_decoded = get_param(response)
rot_13_encoded = codecs.encode(rot_13_decoded, 'rot_13')
nc.send(f"{rot_13_encoded}\n")
response = nc.recv()

"""Decode this binary string and provide me the original number (base 10):"""
binary_str = get_param(response)
int_str = int(binary_str, 2)
nc.send(f"{int_str}\n")
response = nc.recv()

"""Encode this number and provide me the binary equivalent:"""
int_str = get_param(response)
binary_str = bin(int(int_str))
nc.send(f"{binary_str}\n")
response = nc.recv()

"""Final Question, what is the best CTF competition in the universe?"""
nc.send(f"DUCTF\n")
response = nc.recv()
