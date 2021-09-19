print("Starting program")

result = ""
with open("very_old_odd_file1.txt", "rb") as f:
    byte = f.read(1)
    while byte != b"":
        # Do stuff with byte.
        byte = f.read(1)
        if byte == b'\n':
            result += '0'
        elif byte == b'\t':
            result += '1'

i = 0
buffer = bytearray()
while i < len(result):
    buffer.append( int(result[i:i+8], 2) )
    i += 8

# now write your buffer to a file
with open('binary_file', 'bw') as f:
    f.write(buffer)



print("Complete")