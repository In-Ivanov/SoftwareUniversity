message = input()

while True:
    commands = input()
    if commands == "Reveal":
        break
    command = commands.split(":|:")
    action = command[0]

    if action == "InsertSpace":
        index = int(command[1])
        message = message[:index] + " " + message[index:]
        print(message)

    if action == "Reverse":
        substring = command[1]
        if substring in message:
            reverse_string = substring[::-1]
            message = message.replace(substring, reverse_string, 1)
            print(message)
        else:
            print("error")
            continue
    if action == "ChangeAll":
        sub = command[1]
        rep = command[2]
        message = message.replace(sub, rep)
        print(message)


print(f"You have a new text message: {message}")

