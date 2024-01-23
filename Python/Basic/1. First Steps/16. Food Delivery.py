chicken_menu = int(input())
fish_menu = int(input())
meat_menu = int(input())

chicken = 10.35
fish = 12.40
meat = 8.15
delivery = 2.50
all_menu = (chicken_menu * chicken) + (fish_menu * fish) + (meat_menu * meat)
dessert = all_menu * 20 / 100

price = all_menu + dessert + delivery

print(f'{price:.2f}')



