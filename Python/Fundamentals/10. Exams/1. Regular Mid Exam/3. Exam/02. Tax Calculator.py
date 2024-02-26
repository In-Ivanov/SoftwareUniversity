import math

vehile = input().split(">>")


tax_car = 0
total_tax = 0

for car in vehile:
    tax_car = 0
    car_1 = car.split(" ")
    if car_1[0] == "family":
        tax_car += 50 - int(car_1[1]) * 5
        tax_car += math.floor(int(car_1[2]) / 3000) * 12
        total_tax += tax_car
        print(f"A {str(car_1[0])} car will pay {tax_car:.2f} euros in taxes.")

    elif car_1[0] == "heavyDuty":
        tax_car += 80 - int(car_1[1]) * 8
        tax_car += math.floor(int(car_1[2]) / 9000) * 14
        total_tax += tax_car
        print(f"A {str(car_1[0])} car will pay {tax_car:.2f} euros in taxes.")

    elif car_1[0] == "sports":
        tax_car += 100 - int(car_1[1]) * 9
        tax_car += math.floor(int(car_1[2]) / 2000) * 18
        total_tax += tax_car
        print(f"A {str(car_1[0])} car will pay {tax_car:.2f} euros in taxes.")

    else:
        print("Invalid car type.")
        continue

print(f"The National Revenue Agency will collect {total_tax:.2f} euros in taxes." )

