number = int(input())
cars = {}
mil = "miliage"
fuel = "fuel"
tank = 75
for n in range(number):
    car = input().split("|")
    cars[car[0]] = {}
    cars[car[0]][mil] = int(car[1])
    cars[car[0]][fuel] = int(car[2])

while True:
    command = input()
    if command == "Stop":
        break

    com = command.split(" : ")
    action = com[0]
    name = com[1]

    if action == "Drive":
        if int(com[3]) <= cars[name][fuel]:
            cars[name][fuel] -= int(com[3])
            cars[name][mil] += int(com[2])
            print(f"{name} driven for {com[2]} kilometers. {com[3]} liters of fuel consumed.")
            if cars[name][mil] >= 100000:
                del cars[name]
                print(f"Time to sell the {name}!")
        else:
            print("Not enough fuel to make that ride")

    elif action == "Refuel":
        if (cars[name][fuel] + int(com[2])) >= tank:
            refuel = tank - cars[name][fuel]
            cars[name][fuel] = tank
            print(f"{name} refueled with {refuel} liters")
        else:
            cars[name][fuel] += int(com[2])
            print(f"{name} refueled with {com[2]} liters")

    elif action == "Revert":
        cars[name][mil] -= int(com[2])
        if cars[name][mil] > 10000:
            print(f"{name} mileage decreased by {com[2]} kilometers")
        else:
            cars[name][mil] = 10000


for kar in cars.keys():
    print(f"{kar} -> Mileage: {cars[kar][mil]} kms, Fuel in the tank: {cars[kar][fuel]} lt.")
