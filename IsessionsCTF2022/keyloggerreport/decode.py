file = open('log.txt', 'rb')

contents = file.readlines()

generated_str = []
for line in contents:
    command = line.strip().decode().split('-')[-1].strip()
    if command == 'Key.enter':
        generated_str += '\n'
    elif command == 'Key.space':
        generated_str += ' '
    elif command == 'Key.backspace':
        generated_str = generated_str[0:-1]
    elif command == 'Key.shift_r':
        pass
    else:
        generated_str += chr(int(command))
    
    # breakpoint()
    
breakpoint()
