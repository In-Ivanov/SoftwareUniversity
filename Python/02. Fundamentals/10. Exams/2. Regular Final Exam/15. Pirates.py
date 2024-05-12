spell = input()
command = input()
while True:

    if command == "Abracadabra":
        break
    com = command.split()
    action = com[0]
    valid_actions = ["Abjuration", "Necromancy", "Illusion", "Divination", "Alteration"]
    if action in valid_actions:
        if action == "Abjuration":
            spell = spell.upper()
            print(spell)
        if action == "Necromancy":
            spell = spell.lower()
            print(spell)
        if action == "Illusion":
            index = int(com[1])
            if index in range(len(spell)):
                spell = spell.replace(spell[index], com[2])
                print("Done!")
            else:
                print("The spell was too weak.")

        if action == "Divination":
            if com[1] in spell:
                spell = spell.replace(com[1], com[2])

        if action == "Alteration":
            if com[1] in spell:
                spell = spell.replace(com[1], "")
                print(spell)
    else:
        print("The spell did not work!")
    command = input()
