def rotate(c, n):
    x = ord(c) + n
    while x>ord('Z'):
        x -= 26
    return chr(x)

f = open('./names_list.txt', 'r')
contents = f.read()

entries = contents.split('\n')

initials = ''
for entry in entries:
    name = entry.split('\t')[0]
    email = entry.split('\t')[1]
    initial = name.split(' ')[0][0] + name.split(' ')[1][0]
    initials += initial

f = open('./names_list_2.txt', 'r')
contents = f.read()

entries = contents.split('\n')

initials2 = ''
for entry in entries:
    name = entry.split('\t')[0]
    email = entry.split('\t')[1]
    initial = name.split(' ')[0][0] + name.split(' ')[1][0]
    initials2 += initial
    
breakpoint()

lunar_primes = [
    19,29,39,49,59,69,79,89,90,91,92,93,94,95,96,97,
    98,99,109,209,219,309,319,329,409,419,429,439,509,
    519,529,539,549,609,619,629,639,649,659,709,719,
    729,739,749,759,769,809,819,829,839,849,859,869,
    879,901,902,903,904,905,906,907,908,909,912,913,
    914,915,916,917,918,919,923,924,925,926,927,928,
    929,934,935,936,937,938,939,945,946,947,948,949,
    956,957,958,959,967,968,969,978,979,989
]

fortune_numbers = [
    3,5,7,13,17,19,23,37,47,59,61,67,71,79,89,101,
    103,107,109,127,151,157,163,167,191,197,199,223,
    229,233,239,271,277,283,293,307,311,313,331,353,
    373,379,383,397,401,409,419,421,439,443,457,461,
    491,499,509
]

valid_numbers = []

for fortune_num in fortune_numbers:
    if fortune_num in lunar_primes:
        continue
    else:
        valid_numbers.append(fortune_num)

# breakpoint()

rotated_initials = ""
# for c in initials:
#     current_value = ord(c) - 64
#     if fortune_numbers[current_value] in lunar_primes:
#         rotated_initials += c
#     else:
#         rotated_initials += rotate(c, fortune_numbers[current_value])

for c in initials:
    current_value = ord(c) - 65
    rotated_initials += rotate(c, valid_numbers[current_value])

print(rotated_initials)

breakpoint()