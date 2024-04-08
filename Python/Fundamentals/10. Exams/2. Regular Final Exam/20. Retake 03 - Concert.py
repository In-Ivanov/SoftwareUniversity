band = {}
name = "name"
time = "time"
while True:
    command = input()

    if command == "Start!":
        break

    com = command.split("; ")
    action = com[0]

    if action == "Add":
        if com[1] not in band:
            band[com[1]] = {}
            band[com[1]][name] = com[2].split(", ")
            band[com[1]][time] = 0
        else:
            art = com[2].split(", ")
            for i in art:
                if i in band[com[1]][name]:
                    continue
                else:
                    (band[com[1]][name]).append(i)

    if action == "Play":
        if com[1] not in band:
            band[com[1]] = {}
            band[com[1]][name] = []
            band[com[1]][time] = int(com[2])
        else:
            band[com[1]][time] += int(com[2])

count = 0
for key in band.keys():
    count += band[key][time]
print(f"Total time: {count}")

for k in band.keys():
    print(f"{k} -> {band[k][time]}")
for i in band.keys():
    print(i)
    for l in band[i][name]:
        print(f"=> {l}")
    break




