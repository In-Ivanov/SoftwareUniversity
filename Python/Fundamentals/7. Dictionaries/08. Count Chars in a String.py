text = input().split(" ")
textt = {}
for t in text:
    for i in t:
       if i not in textt:
           textt[i] = 0
       textt[i] += 1
for key, value in textt.items():
    print(f"{key} -> {value}")


