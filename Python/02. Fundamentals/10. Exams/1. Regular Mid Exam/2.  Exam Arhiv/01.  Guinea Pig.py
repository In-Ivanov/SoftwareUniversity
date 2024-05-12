food_kg = float(input()) * 1000
hay_kg = float(input()) * 1000
cover_kg = float(input()) * 1000
weight_g = float(input()) * 1000


for day in range(1, 31):
    food_kg -= 300
    if day % 2 == 0:
        hay_kg -= (food_kg * 0.05)

    if day % 3 == 0:
        cover_kg -= (weight_g * (1 / 3))
if food_kg <= 0 or hay_kg <= 0 or cover_kg <= 0:
    print("Merry must go to the pet store!")
else:
    print(f"Everything is fine! Puppy is happy! Food: {((food_kg) / 1000):.2f}, Hay: {((hay_kg) / 1000):.2f}, Cover: {((cover_kg) / 1000):.2f}.")


