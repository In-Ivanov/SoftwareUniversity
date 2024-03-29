new = input()
ih = list(map(str, new))
for i in ih:
    if i == ":":
        index = ih.index(":")
        print(f"{ih[index]}{ih[index + 1]}")
        ih[index] = "q"
        del index
    else:
        continue


