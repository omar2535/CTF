from public import flag_public

# Finds based on fake element in flag_public
# Returns the index and the actual key element since they are grouped by (fake, key) or (key, fake)
def find_element(ele, public):
    for index, pair in enumerate(public):
        if pair[0] == ele:
            return (index, pair[1]) # Return the index and the key
        elif pair[1] == ele:
            return (index, pair[0]) # Return the index and the key
    raise "Not found exception"

ln = len(flag_public)
cur_public = flag_public
key = [0] * ln

# Find the eleemtn, get key, then remove element from current public
ele = find_element(0, cur_public)
key[-1] = ele[1]
del cur_public[ele[0]]

# Lets start finding the keys now
for i in range(-2, -ln-1, -1):
    fake = 0
    # Generate the fake
    for j in range(1, 201):
        index = i + j
        if index >= 0:
            break
        fake = fake ^ key[index]
    
    # Find the key:
    ele = find_element(fake, cur_public)
    key[i] = ele[1]
    del cur_public[ele[0]]

print(key)

# IE. Key length is 20
# fake[19] = 0, we can find key[19]
# fake[18] = fake[18] ^ key[19]
# fake[17] = fake[17] ^ key[18] ^ key[19]
