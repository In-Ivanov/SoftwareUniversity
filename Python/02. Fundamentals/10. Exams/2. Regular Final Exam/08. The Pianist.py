number_of_pieces = int(input())
pieces = {}

for _ in range(number_of_pieces):
    song = input().split("|")
    piece, composer, key = song[0], song[1], song[2]
    pieces[piece] = {}
    pieces[piece][composer] = key

while True:
    piec = input()
    if piec == "Stop":
        break
    command = piec.split("|")
    action = command[0]

    if action == "Add":
        if command[1] not in pieces.keys():
            pieces[command[1]] = {}
            pieces[command[1]][command[2]] = command[3]
            print(f"{command[1]} by {command[2]} in {command[3]} added to the collection!")
        else:
            print(f"{command[1]} is already in the collection!")

    if action == "Remove":
        if command[1] in pieces:
            del pieces[command[1]]
            print(f"Successfully removed {command[1]}!")
        else:
            print(f"Invalid operation! {command[1]} does not exist in the collection.")

    if action == "ChangeKey":
        if command[1] in pieces.keys():
                for keys, value in pieces[command[1]].items():
                    value = command[2]
                    pieces[command[1]][keys] = value
                print(f"Changed the key of {command[1]} to {command[2]}!")
        else:
            print(f"Invalid operation! {command[1]} does not exist in the collection.")

for pi in pieces.keys():
    for k, v in pieces[pi].items():
        print(f"{pi} -> Composer: {k}, Key: {v}")
