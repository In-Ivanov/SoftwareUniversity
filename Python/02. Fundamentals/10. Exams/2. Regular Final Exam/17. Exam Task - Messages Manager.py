capacity = int(input())

names = {}
sent = "sent"
received = "received"

while True:
    command = input()

    if command == "Statistics":
        break

    me = command.split("=")
    action = me[0]

    if action == "Add":
        if me[1] not in names:
            names[me[1]] = {}
            names[me[1]][sent] = int(me[2])
            names[me[1]][received] = int(me[3])

    if action == "Message":
        if  me[1] and me[2] in names:
            names[me[1]][sent] += 1
            names[me[2]][received] += 1
            if names[me[1]][sent] + names[me[1]][received] >= capacity:
                del names[me[1]]
                print(f"{me[1]} reached the capacity!")

            if names[me[2]][sent] + names[me[2]][received] >= capacity:
                del names[me[2]]
                print(f"{me[2]} reached the capacity!")

    if action == "Empty":
        if me[1] in names:
            del names[me[1]]
        if me[1] == "All":
            names.clear()

print(f"Users count: {len(names.keys())}")
for nam in names.keys():
    print(f"{nam} - {names[nam][sent] + names[nam][received]}")