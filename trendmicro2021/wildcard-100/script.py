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

result_split = [result[i:i+8] for i in range(0, len(result), 8)]
print(result_split)
breakpoint()


print("Complete")