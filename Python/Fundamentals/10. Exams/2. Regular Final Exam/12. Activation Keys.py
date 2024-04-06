keys = input()


while True:
    command = input()
    if command == "Generate":
        break

    activation = command.split(">>>")
    action = activation[0]

    if action == "Contains":
        if activation[1] in keys:
            print(f"{keys} contains {activation[1]}")
        else:
            print("Substring not found!")
    if action == "Flip":
        start_index = int(activation[2])
        end_index = int(activation[3])
        if activation[1] == "Upper":
            new_key = keys[start_index:end_index]
            keys= keys.replace(new_key, new_key.upper())
            print(keys)

        elif  activation[1] == "Lower":
            new_key = keys[start_index:end_index]
            keys = keys.replace(new_key, new_key.lower())
            print(keys)

    if action == "Slice":
        s_index = int(activation[1])
        e_index = int(activation[2])
        n_key = keys[s_index:e_index]
        keys = keys.replace(n_key, "",1)
        print(keys)

print(f"Your activation key is: {keys}")


