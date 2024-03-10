text = input().split(" ")
num = 0
num1 = 0
for txt in text[0]:
    for i in txt:
        num += ord(i)

for txt in text[1]:
    for i in txt:
        num1 += ord(i)

print(num * num1)

