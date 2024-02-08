string = input()
new = ""

while string != "End":
    for i in string:
        new += i * 2
    print(new)
    new = ""
    string = input()
    if string == "SoftUni":
        string = input()



