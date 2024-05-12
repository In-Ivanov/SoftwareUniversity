number = int(input())
perfect = 0

for num in range(1, number):
    if number % num == 0:
        perfect += num

if perfect == number:
    print("We have a perfect number!")
else:
    print("It's not so perfect.")

