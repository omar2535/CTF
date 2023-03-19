from rich.console import Console

console = Console()

user_input = list(str(console.input(":arrow_right_hook: ")).lower())
a = [124, 123, 135, 136, 116, 128, 128, 137, 116, 121, 123, 123, 120, 111, 117, 124, 123, 111, 113, 125, 111, 110, 106, 115]
for i in range(len(user_input)):
    user_input[i] = ord(user_input[i]) + i

passwd = a[::-1]
for i in range(len(passwd)):
    passwd[i] = chr(passwd[i]-i)

breakpoint()
