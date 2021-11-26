#!/usr/bin/env python3

import random
from public import flag_public
from enc import flag_enc

def keygen(ln):
    # Generate a linearly independent key
    arr = [ 1 << i for i in range(ln) ]

    for i in range(ln):
        for j in range(i):
            if random.getrandbits(1):
                arr[j] ^= arr[i]
    for i in range(ln):
        for j in range(i):
            if random.getrandbits(1):
                arr[ln - 1 - j] ^= arr[ln - 1 - i]

    return arr

def gen_keystream(key):
    ln = len(key)
    
    # Generate some fake values based on the given key...
    fake = [0] * ln
    for i in range(ln):
        for j in range(ln // 3):
            if i + j + 1 >= ln:
                break
            fake[i] ^= key[i + j + 1]

    # Generate the keystream
    res = []
    for i in range(ln):
        t = random.getrandbits(1)
        if t:
            res.append((t, [fake[i], key[i]]))
        else:
            res.append((t, [key[i], fake[i]]))

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


def brute_force_decode():
    enc = bytes_to_bits(bytes.fromhex(flag_enc))
    flag = attempt_decode(enc)

def attempt_decode(enc):
    while True:
        length_of_flag = 600
        key = keygen(length_of_flag)

        keystream, public = gen_keystream(key)
        if (keystream != recover_keystream(key, public)):
            continue

        if public == flag_public:
            breakpoint()
            flag = bits_to_bytes(xor(keystream, enc))
            print(flag)
            return flag

def encode():
    flag = bytes_to_bits(flag)

    key = keygen(len(flag))                              # KEYGEN is only based on length!!
                                                         # We know the length of the flag!

    breakpoint()
    keystream, public = gen_keystream(key)               # Generate the keystream
    assert keystream == recover_keystream(key, public)   

    enc = bits_to_bytes(xor(flag, keystream))            # ONE TIME PAD

    print(enc.hex())
    print(public)

brute_force_decode()