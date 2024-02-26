import math

biscuits = int(input())
workers = int(input())
all_biscuits = int(input())
final_bisc = 0
not_full = 0
bis = int(math.floor(biscuits * workers))
day_bisc = int(math.floor(bis * 0.75))

for day in range(30):

    if day % 3 == 0:
        not_full += 1

full_day_bisc = 30 - not_full
month = full_day_bisc * bis + day_bisc * not_full
difference = month - all_biscuits
percent = difference / all_biscuits * 100
print(f"You have produced {month} biscuits for the past month.")
if difference > 0:
    print(f"You produce {percent:.2f} percent more biscuits.")
else:
    percent = (abs(difference) / all_biscuits) * 100
    print(f"You produce {percent:.2f} percent less biscuits.")
