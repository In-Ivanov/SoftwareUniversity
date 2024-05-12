number = int(input())
users = {}
while True:

    for com in range(number):
        command = input().split()
        if command[0] == "register":
            if command[1] not in users.keys():
                users[command[1]] = command[2]
                print(f"{command[1]} registered {command[2]} successfully")
            elif command[1] in users.keys():
                print(f"ERROR: already registered with plate number {users[command[1]]}")
        if command[0] == "unregister":
            if command[1] not in users.keys():
                print(f"ERROR: user {command[1]} not found")
            elif command[1] in users.keys():
                del users[command[1]]
                print(f"{command[1]} unregistered successfully")
    break

for (v, k) in users.items():
    print(f"{v} => {k}")

