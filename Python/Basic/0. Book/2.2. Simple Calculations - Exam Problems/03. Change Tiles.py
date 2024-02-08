lenght_landing = float(input())
width_tile = float(input())
lenght_tile = float(input())
width_a_bench = float(input())
lenght_a_bench = float(input())

land = lenght_landing * lenght_landing
bench = width_a_bench * lenght_a_bench
tile = width_tile * lenght_tile
all_land = land - bench
all_tile = all_land / tile

time_for_all_tile = all_tile * 0.2

print(f"{all_tile:.2f}")
print(f"{time_for_all_tile:.2f}")


