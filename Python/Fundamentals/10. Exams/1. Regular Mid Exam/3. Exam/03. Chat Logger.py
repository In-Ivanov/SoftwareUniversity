chat = list(input().split(" "))
new_chat = []

while chat[0] != "end":
    command = chat[0]
    message = chat[1]
    if command == "Chat":
        if message not in new_chat:
            new_chat.append(message)
    elif command == "Delete":
        if message in new_chat:
            new_chat.remove(message)
    elif command == "Edit":
        if message in new_chat:
            new_chat.remove(message)
            new_chat.append(chat[2])
    elif command == "Pin":
        if message in new_chat:
            new_chat.remove(message)
            new_chat.append(message)

    elif command == "Spam":
        chat.remove(command)
        new_chat.extend(chat)

    chat = list(input().split(" "))
print(*new_chat, sep="\n")
