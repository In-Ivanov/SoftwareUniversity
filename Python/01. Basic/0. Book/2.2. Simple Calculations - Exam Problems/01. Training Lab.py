length = float(input()) * 100
width = float(input()) * 100

length_one = length // 120
width_one = (width - 100) // 70
all_places = length_one * width_one - 3

print(int(all_places))

