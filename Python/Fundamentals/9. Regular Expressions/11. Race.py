import re
name = ""
km = 0
users = {}
gamers = input().split(", ")
pattern1 = r"([a-z-A-Z]{1})"
pattern2 = r"(\d{1})"
while True:
    info = input()
    km = 0
    if info == "end of race":
        break

    x = re.findall(pattern1, info)
    y = re.findall(pattern2, info)
    name = "".join(x)
    for i in y:
        km += int(i)

    if name not in gamers:
        continue
    else:
        if name not in users.keys():
            users[name] = km
        else:
            users[name] += km

users1 = sorted(users.items(), key=lambda x:x[1], reverse=True)
converted_dict = dict(users1)
m = 0
count = 0
while True:

    for key, value in converted_dict.items():
        count += 1

        if count == 1:
            print(f"1st place: {key}")
        if count == 2:
            if m == value:
                count -= 1
                print(f"1st place: {key}")
            else:
                print(f"2nd place: {key}")

        if count == 3:
            if m == value:
                count -= 1
                print(f"2nd place: {key}")
            else:
                print(f"3rd place: {key}")

        if count == 4:
            if m == value:
                count -= 1
                print(f"3rd place: {key}")
            else:
                break
        m = value
    break



