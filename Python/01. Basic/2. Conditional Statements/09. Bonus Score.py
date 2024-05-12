number = int(input())
number_bonus = 0

if number <= 100:
    number_bonus += 5
    if number % 2 == 0:
        number_bonus += 1
    if number % 5 == 0 and number % 2 != 0:
        number_bonus += 2
if 100 < number < 1000:
    number_bonus += (number * 0.2)
    if number % 2 == 0:
        number_bonus += 1
    if number % 5 == 0 and number % 2 != 0:
        number_bonus += 2
if number > 1000:
    number_bonus += (number * 0.1)
    if number % 2 == 0:
        number_bonus += 1
    if number % 5 == 0 and number % 2 != 0:
        number_bonus += 2
print(number_bonus)
print(number + number_bonus)

