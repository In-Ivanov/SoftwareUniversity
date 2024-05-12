output = ''
in_char = None
string = input()
for char in string:
    if char != in_char:
        output += char
        in_char = char

print(output)
