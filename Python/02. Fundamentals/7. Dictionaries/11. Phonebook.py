contact = input()
book = {}
while "-" in contact:
    info = contact.split("-")
    if info[0] not in book:
        book[info[0]] = info[1]
    else:
        book[info[0]] = info[1]
    contact = input()
num = int(contact)
for i in range(0, num):
    contact = input()
    if contact in book.keys():
        print(f"{contact} -> {book[contact]}")
    else:
        print(f"Contact {contact} does not exist.")



