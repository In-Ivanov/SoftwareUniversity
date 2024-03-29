import re

def ad_astra(string_data):
    pattern = r"(\#|\|)([A-z-a-z-\s]{1,})\1([\d]{2}\/[\d]{2}\/[\d]{2})\1([\d]{,5})\1"
    item = {}
    days = 0
    result = re.finditer(pattern, string_data)

    for food in result:
        item[food.group(2)] = {}
        item[food.group(2)][food.group(3)] = food.group(4)
        days += int(food.group(4))
    if days > 0:
        last_days = int(days / 2000)
        print(f"You have food to last you for: {last_days} days!")
    else:
        print(f"You have food to last you for: {days} days!")

    for (key, value) in item.items():
        for k, v in value.items():
            print(f"Item: {key}, Best before: {k}, Nutrition: {v}")

string = input()
star = ad_astra(string)


'''
import re

food_information = input()
pattern = r"(?i)([#|])([a-z\s]+)\1(\d{2}\/\d{2}\/\d{2})\1(\d+)\1"
matches = re.findall(pattern, food_information)
total_calories = sum([int(match[3]) for match in matches])
days = total_calories // 2000
print(f"You have food to last you for: {days} days!")
for element in matches:
    item_name = element[1]
    expiration_date = element[2]
    item = element[3]
    print(f"Item: {item_name}, Best before: {expiration_date}, Nutrition: {item}")

'''


