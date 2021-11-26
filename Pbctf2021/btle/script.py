import csv

with open('export.csv', newline='') as csvfile:
    data = list(csv.reader(csvfile))

headers = data[0]
data = data[1:]
value_index = headers.index("Value")
offset_index = headers.index("Offset")

constructed_string = " " * 60

for packet in data:
    offset = int(packet[offset_index])
    value = bytearray.fromhex(packet[value_index]).decode()
    constructed_string = constructed_string[:offset] + value + constructed_string[len(value) + offset:]
    # breakpoint()

breakpoint()
print(constructed_string)

# pctf{}