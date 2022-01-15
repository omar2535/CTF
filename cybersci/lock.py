import nclib
import base64
import codecs
from urllib.parse import unquote


def main():
    nc = nclib.Netcat(('10.0.1.33', 10001), verbose=True)

    # Initial connection
    response = nc.recv()
    response = nc.recv()

    keypad = response.decode('utf-8').split('|')
    
    number_of_missing_numbers = 0
    numbers = []
    for string in keypad:
        if string == ' ** ':
            number_of_missing_numbers += 1
        try:
            numbers.append(int(string))
        except Exception as e:
            pass

    # sort the numbers
    numbers.sort()
    
    missing_numbers = find_missing_numbers(numbers)
    assert len(missing_numbers) == number_of_missing_numbers

    print(missing_numbers)
    payload = generate_payload(missing_numbers)
    
    # Send the enter
    
    nc.send(payload)
    response = nc.recv()

    breakpoint()
    

def generate_payload(missing_numbers):
    payload = ""
    for number in missing_numbers:
        payload += str(number) + " "
    payload = payload.rstrip()
    payload += "\n"
    return payload.encode('utf-8')
        

def find_missing_numbers(numbers):
    missing_numbers = []
    for i in range(1, 37):
        if i not in numbers:
            missing_numbers.append(i)
    return missing_numbers



main()