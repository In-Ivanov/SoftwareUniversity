number = int(input())
plants = {}
rating = "Rating"
rarity = "Rarity"
count = "Count"

for pl in range(number):
    plant = input().split("<->")
    plants[plant[0]] = {}
    plants[plant[0]]["Rarity"] = int(plant[1])
    plants[plant[0]]["Rating"] = 0.0
    plants[plant[0]]["Count"] = 0

while True:
    command = input()

    if command == "Exhibition":
        break

    com = command.split(" ")
    action = com[0]
    name = com[1]

    if action == "Rate:":
        if name in plants.keys():
            plants[name][rating] += float(com[3])
            plants[name][count] += 1
            plants[name][rating] = plants[name][rating] / plants[name][count]
        if name not in plants.keys():
            print(f'"error"')

    if action == "Update:":
        if name in plants.keys():
            plants[name][rarity] = int(com[3])
        if name not in plants.keys():
            print(f'"error"')

    if action == "Reset:":
        if name in plants.keys():
            plants[name][rating] = 0.0
        if name not in plants.keys():
            print(f'"error"')

print("Plants for the exhibition:")
for _ in plants.keys():
    name = _
    print(f"- {name}; Rarity: {plants[name][rarity]}; Rating: {(plants[name][rating]):.2f}")

