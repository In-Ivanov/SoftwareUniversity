nylon = int(input())
paint = int(input())
thinner = int(input())
hours = int(input())

price_nylon = 1.50
price_paint = 14.50
price_thinner = 5.00

all_nylon = nylon * price_nylon
all_paint = paint * price_paint
all_thinner = thinner * price_thinner

reserve = (all_paint * 10 / 100) + (2 * price_nylon) + 0.40
all_price = all_nylon + all_paint + all_thinner + reserve
price_human = all_price * 30 / 100
all_work = all_price + (price_human * hours)

print(all_work)

