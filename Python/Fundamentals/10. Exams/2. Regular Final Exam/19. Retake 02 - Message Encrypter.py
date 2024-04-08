import re

num = int(input())

pattern = r"([*]{1}[A-Z][a-z]{2,}[*]{1}[:]{1}[\s]{1})([[][A-za-z][]][|][[][A-Za-z][]][|][[][A-Za-z][]][|])$|([@]{1}[A-Z][a-z]{2,}[@]{1}[:]{1}[\s]{1})([[][A-za-z][]][|][[][A-Za-z][]][|][[][A-Za-z][]][|])$"
op = ""
d = []
for n in range(num):
    command = input()

    if re.search(pattern, command):
        result = re.finditer(pattern, command)
        for match in result:
            op += (match.group())
            op = op.replace("@", "")
            op = op.replace("[", "")
            op = op.replace("]", "")
            op = op.replace("|", "")
            op = op.replace("*", "")
        com = op.split(" ")
        for i in com[1]:
            d.append(ord(i))
        print(f"{com[0]}", *d)
        op = ""
        d = []

    else:
        print("Valid message not found!")
        continue
