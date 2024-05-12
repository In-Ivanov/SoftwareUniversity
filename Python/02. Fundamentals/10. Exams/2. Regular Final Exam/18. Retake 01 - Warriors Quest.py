skill = input()
command = input()
while True:

    if command == "For Azeroth":
        break

    com = command.split(" ")
    action = com[0]
    oh = ["GladiatorStance", "DefensiveStance", "Dispel", "Target"]

    if action in oh:

        if action == "GladiatorStance":
            skill = skill.upper()
            print(skill)

        elif action == "DefensiveStance":
            skill = skill.lower()
            print(skill)

        elif action == "Dispel":
            index = int(com[1])
            if index in range(len(skill)):
                rep = skill[index]
                skill = skill.replace(rep, com[2], 1)
                print("Success!")
            else:
                print("Dispel too weak.")

        elif action == "Target":
            if com[1] == "Change":
                if com[2] in skill:
                    skill = skill.replace(com[2], com[3])
                    print(skill)
                else:
                    print(skill)

            elif com[1] == "Remove":
                if com[2] in skill:
                    skill = skill.replace(com[2], "")
                    print(skill)
    else:
        print("Command doesn't exist!")
    command = input()

