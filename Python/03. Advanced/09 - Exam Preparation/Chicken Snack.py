from collections import deque

money = [int(x) for x in input().split()]

price = deque([int(x) for x in input().split()])

food = 0

while money and price:
    if money[-1] == price[0]:
        food += 1
        money.pop()
        price.popleft()
    elif money[-1] > price[0]:
        food += 1
        difference = money[-1] - price[0]
        money.pop()
        price.popleft()
        if money:
            money[-1] += difference
        else:
            money = [difference]
    else:
        money.pop()
        price.popleft()

if food >= 4:
    print(f"Gluttony of the day! Henry ate {food} foods.")
elif 1 <= food < 4:
    if food == 1:
        print(f"Henry ate: {food} food.")
    else:
        print(f"Henry ate: {food} foods.")
else:
    print(f"Henry remained hungry. He will try next weekend again.")