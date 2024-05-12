vegetable_for_kg = float(input())
fruit_for_kg = float(input())
all_kg_vegetable = int(input())
all_kg_fruit = int(input())

eur = 1.94

vegetable = vegetable_for_kg * all_kg_vegetable
fruit = fruit_for_kg * all_kg_fruit
all_price_eur = (vegetable + fruit) / eur

print(all_price_eur)
