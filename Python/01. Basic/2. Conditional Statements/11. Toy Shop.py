price = float(input())
pyzel = int(input())
dool = int(input())
bear = int(input())
minion = int(input())
truck = int(input())

toys = pyzel + dool + bear + minion + truck
all_price = (pyzel * 2.60) + (dool * 3) + (bear * 4.10) + (minion * 8.20) + (truck * 2)
if toys >= 50:
    all_price -= (all_price * 0.25)
    all_price -= (all_price * 0.10)
    if all_price < price:
        money = price - all_price
        print(f"Not enough money! {money:.2f} lv needed.")
    else:
        money = all_price - price
        print(f"Yes! {money:.2f} lv left.")

else:
    all_price -= (all_price * 0.10)
    if all_price < price:
        money = price - all_price
        print(f"Not enough money! {money:.2f} lv needed.")
    else:
        money = all_price - price
        print(f"Yes! {money:.2f} lv left.")


