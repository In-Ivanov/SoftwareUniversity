string = input()
strenght = 0
output = ''
for char in string:
    if strenght > 0:
        if char.isalpha():
            strenght -= 1
            continue
    if char == ">":
        output += char

    elif char != ">":
        if char.isdigit():
            strenght += int(char)
            strenght -= 1
            continue
        else:
            output += char

print(output)