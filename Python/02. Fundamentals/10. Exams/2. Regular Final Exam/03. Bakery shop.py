counter = 0
bakery = {}

while True:
    command = input()
    if command == "Complete":
        break
    com, quantity, food = command.split()
    quantity = int(quantity)

    if com == "Receive":
        if quantity <= 0:
            continue
        if food in bakery:
            bakery[food] += quantity
        else:
            bakery[food] = 0
            bakery[food] += quantity
    if com == "Sell":
        if food not in bakery:
            print(f"You do not have any {food}.")
        elif quantity > bakery[food]:
            print(f"There aren't enought {food}. You sold the last {bakery[food]} of them.")
            counter += bakery[food]
            del bakery[food]
        elif quantity <= bakery[food]:
            bakery[food] -= quantity
            print(f"You sold {quantity} {food}.")
            counter += quantity
            if bakery[food] == 0:
                del bakery[food]

for food, quantity in bakery.items():
    print(f"{food}: {quantity}")
print(f"All sold: {counter} goods")



