command = input().split(" ")
dictt = {}
for word in command:
    wordd = word.casefold()
    if wordd not in dictt:
        dictt[wordd] = 0
    dictt[wordd] += 1
pol = []
for key, value in dictt.items():
    if value % 2 != 0:
        pol.append(key)
print(" ".join(pol))


