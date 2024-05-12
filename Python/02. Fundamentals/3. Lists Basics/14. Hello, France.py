'''
collection_of_items = list(input().split("|"))
budget = int(input())
item = []
new_price_list = []
profit = 0.0
new_price = 0.0

for index in range(len(collection_of_items)):
    item = collection_of_items[index].split("->")
    if item[0] == "Clothes":
        price_1 = float(item[1])
        if price_1 > 50 or budget < price_1:
            continue
        else:
            budget -= price_1
            profit += round(price_1 * 0.4, 2)
            price_1 = round(price_1 * 1.4, 2)
            new_price += price_1
            new_price_list.append(price_1)
    elif item[0] == "Shoes":
        price_1 = float(item[1])
        if price_1 > 35 or budget < price_1:
            continue
        else:
            budget -= price_1
            profit += round(price_1 * 0.4, 2)
            price_1 = round(price_1 * 1.4, 2)
            new_price += price_1
            new_price_list.append(price_1)
    elif item[0] == "Accessories":
        price_1 = float(item[1])
        if price_1 > 20.5 or budget < price_1:
            continue
        else:
            budget -= price_1
            profit += round(price_1 * 0.4, 2)
            price_1 = round(price_1 * 1.4, 2)
            new_price += price_1
            new_price_list.append(price_1)

new_budget = new_price + budget
print(*new_price_list)
print(f"Profit: {profit:.2f}")

if new_budget > 150:
    print("Hello, France!")
else:
    print("Not enough money.")

'''





items = input().split('|')
budget = int(input())
bought_items = []

for i in items:
    item = i.split('->')
    valid = False
    item_price = float(item[1])

    if item[0] == 'Clothes' and item_price <= 50:
        valid = True
    elif item[0] == 'Shoes' and item_price <= 35:
        valid = True
    elif item[0] == 'Accessories' and item_price <= 20.50:
        valid = True

    if valid:
        if budget - item_price < 0:
            break

        budget -= item_price
        bought_items.append(item_price)

items_with_profit = [item * 1.4 for item in bought_items]

for item in items_with_profit:
    print(f'{item:.2f}', end=' ')

print()
print(f'Profit: {abs(sum(bought_items) - sum(items_with_profit)):.2f}')
if sum(items_with_profit) + budget >= 150:
    print('Hello, France!')
else:
    print('Not enough money.')