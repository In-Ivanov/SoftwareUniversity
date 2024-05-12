wagons = [0] * int(input())

while True:
    command = input().split()

    if command[0] == "End":
        print(wagons)
        break

    elif command[0]  == "add":
        number_of_people = int(input())
        wagons