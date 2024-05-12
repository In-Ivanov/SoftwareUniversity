
"""
coffee = 0

while True:
    command = input()
    if command == "END":
        break
    if command == "coding" or command == "dog" or command == "cat" or command == "movie":
        coffee += 1
    elif command == "CODING" or command == "DOG" or command == "CAT" or command == "MOVIE":
        coffee += 2
if coffee < 5:
    print(coffee)
else:
    print("You need extra sleep")

"""

action = input()

coffees = 0

action_to_lower = ['coding', 'movie', 'dog', 'cat']
action_to_upper = ['CODING', 'MOVIE', 'DOG', 'CAT']

while action != 'END':

    if action in action_to_lower:
        coffees += 1
    elif action in action_to_upper:
        coffees += 2

    action = input()

    if action == 'END':
        if coffees > 5:
            print('You need extra sleep')
        else:
            print(coffees)