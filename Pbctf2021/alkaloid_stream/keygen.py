import random

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



key = keygen(1)
breakpoint()