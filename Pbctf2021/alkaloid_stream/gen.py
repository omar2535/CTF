#!/usr/bin/env python3

import random

flag = b"pbctf{stuf}"

def keygen(ln):
    # Generate a linearly independent key
    arr = [ 1 << i for i in range(ln) ]                                 # [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, ...]

    for i in range(ln):
        for j in range(i):
            if random.getrandbits(1):
                arr[j] = arr[j] ^ arr[i]                                # XOR parts of the array with itself from the front

    for i in range(ln):
        for j in range(i):
            if random.getrandbits(1):
                arr[ln - 1 - j] = arr[ln - 1 - j] ^ arr[ln - 1 - i]     # XOR parts of the array with itself from the back

    return arr

def gen_keystream(key):
    ln = len(key)
    
    # Generate some fake values based on the given key...
    fake = [0] * ln                                      # fake = [0, 0, 0, 0, ..., 0] with length of bitstring key
    for i in range(ln):                                  # Loop through the length of the key
        for j in range(ln // 3):
            if i + j + 1 >= ln:
                break
            fake[i] = fake[i] ^ key[i + j + 1]          
            
    # IE. Key length is 20
    # fake[19] = 0, we can find key[19]
    # fake[18] = fake[18] ^ key[19]


    breakpoint()

    # Generate the keystream
    res = []
    for i in range(ln):
        t = random.getrandbits(1)
        if t:
            # when t=1
            res.append((t, [fake[i], key[i]]))
        else:
            # when t=0
            res.append((t, [key[i], fake[i]]))

    breakpoint()
    # Shuffle!
    random.shuffle(res)

    keystream = [v[0] for v in res]
    public = [v[1] for v in res]
    return keystream, public

def xor(a, b):
    return [x ^ y for x, y in zip(a, b)]

def recover_keystream(key, public):
    st = set(key)
    keystream = []
    for v0, v1 in public:
        if v0 in st:
            keystream.append(0)
        elif v1 in st:
            keystream.append(1)
        else:
            assert False, "Failed to recover the keystream"
    return keystream

def bytes_to_bits(inp):
    res = []
    for v in inp:
        res.extend(list(map(int, format(v, '08b'))))
    return res

def bits_to_bytes(inp):
    res = []
    for i in range(0, len(inp), 8):
        res.append(int(''.join(map(str, inp[i:i+8])), 2))
    return bytes(res)

flag = bytes_to_bits(flag)

key = keygen(len(flag))                              # KEYGEN is only based on length!!
                                                     # Length of key is 1200

breakpoint()
keystream, public = gen_keystream(key)               # Generate the keystream
assert keystream == recover_keystream(key, public)   

enc = bits_to_bytes(xor(flag, keystream))            # ONE TIME PAD

print(enc.hex())
print(public)

breakpoint()
