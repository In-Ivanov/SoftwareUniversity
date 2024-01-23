tax = int(input())

sneakers = tax - (tax * 40 / 100)
outfit = sneakers - (sneakers * 20 / 100)
ball = 0.25 * outfit
accessories = 0.2 * ball

all_price = tax + sneakers + outfit + ball + accessories

print(all_price)
