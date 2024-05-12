num = int(input())
string = ""
for i in range(num):
    string = input()
    if "," in string or "." in string or "_" in string:
        print(f"{string} is not pure!")

    else:
        print(f"{string} is pure.")
