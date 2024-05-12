num = int(input())
heroes = {}
maximum_hp = 100
maximum_mp = 200
for i in range(num):
    hero = input().split()
    heroes[hero[0]] = {}
    heroes[hero[0]]["hp"] = (int(hero[1]))
    heroes[hero[0]]["mp"] = (int(hero[2]))

while True:
    command = input()
    if command == "End":
        break
    commands = command.split(" - ")
    action = commands[0]
    hero_name = commands[1]
    if action == "CastSpell":
        if heroes[hero_name]["mp"] >= int(commands[2]):
            heroes[hero_name]["mp"] -= int(commands[2])
            a = heroes[hero_name]["mp"]
            print(f"{hero_name} has successfully cast {commands[3]} and now has {a} MP!")
        else:
            print(f"{hero_name} does not have enough MP to cast {commands[3]}!")
    if action == "TakeDamage":
        if int(heroes[hero_name]["hp"] - int(commands[2])) > 0:
            heroes[hero_name]["hp"] -= int(commands[2])
            a = heroes[hero_name]["hp"]
            print(f"{hero_name} was hit for {commands[2]} HP by {commands[3]} and now has {a} HP left!")

        else:
            print(f"{hero_name} has been killed by {commands[3]}!")
            del heroes[hero_name]

    if action == "Recharge":
        ih = heroes[hero_name]["mp"]
        heroes[hero_name]["mp"] += int(commands[2])
        if heroes[hero_name]["mp"] > 200:
            hm = 200 - ih
            print(f"{hero_name} recharged for {hm} MP!")
            heroes[hero_name]["mp"] = 200
        else:
            print(f"{hero_name} recharged for {commands[2]} MP!")

    if action == "Heal":
        uh = heroes[hero_name]["hp"]
        heroes[hero_name]["hp"] += int(commands[2])
        if heroes[hero_name]["hp"] > 100:
            oh = 100 - uh
            heroes[hero_name]["hp"] = 100
            print(f"{hero_name} healed for {oh} HP!")
        else:
            print(f"{hero_name} healed for {commands[2]} HP!")


for m in heroes.keys():
    b = heroes[m]["hp"]
    c = heroes[m]["mp"]
    print(f"{m}\n  HP: {b}\n  MP: {c}")


