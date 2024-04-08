num = int(input())
name = ""
age = ""
for i in range(num):
    text = input().split(" ")
    for n in text:
        if "@" and "|" in n:
            name = n
            index_n1 = name.index("@")
            index_n2 = name.index("|")
            name = name[index_n1 + 1:index_n2]

        if "#" and "*" in n:
            age = n
            index_a1 = age.index("#")
            index_a2 = age.index("*")
            age = age[index_a1 + 1:index_a2]

    print(f"{name} is {age} years old.")


