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

result_split = [result[i:i+5] for i in range(0, len(result), 5)]

result_stats_mapper = {}

# Print out resulting string
resulting_string = ""
for bit_string in result_split:
    if bit_string in result_stats_mapper:
        result_stats_mapper[bit_string] += 1
    else:
        result_stats_mapper[bit_string] = 1
    
    resulting_string += bit_string + " "

print(resulting_string)
print(result_stats_mapper)

print("Complete")