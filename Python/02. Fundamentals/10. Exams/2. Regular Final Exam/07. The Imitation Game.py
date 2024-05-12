encripted_message = input()
decrypted_message = ''
while True:
    end = input()
    if end == "Decode":
        break
    command = end.split("|")
    action = command[0]

    if action == "Move":
        n = encripted_message[:int(command[1])]
        decrypted_message = encripted_message.replace(n, "")
        decrypted_message += n
        encripted_message = decrypted_message
    if action == "Insert":
        index = int(command[1])
        encripted_message = encripted_message[:index] + command[2] + encripted_message[index:]

    if action == "ChangeAll":
        encripted_message = encripted_message.replace(command[1], command[2])

print(f"The decrypted message is: {encripted_message}")
