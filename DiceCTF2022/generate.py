from Crypto.Util.number import getPrime, bytes_to_long, long_to_bytes

def getAnnoyingPrime(nbits, e):
	while True:
		p = getPrime(nbits)
		if (p-1) % e**2 == 0: # if (p-1) % (e^2) == 0
			return p

nbits = 128
e = 17

p = getAnnoyingPrime(nbits, e)
q = getAnnoyingPrime(nbits, e)

print(p)
print(q)

flag = b"dice{???????????????????????}"

N = p * q
cipher = pow(bytes_to_long(flag), e, N)

print(f"N = {N}")
print(f"e = {e}")
print(f"cipher = {cipher}")



# decrypt
phi = (p-1) * (q-1)

# e * d = 1 mod (phi(n))
key = pow(e, -1, phi)
breakpoint()

plaintext = pow(cipher, key, N)
result = long_to_bytes(plaintext)


breakpoint()
