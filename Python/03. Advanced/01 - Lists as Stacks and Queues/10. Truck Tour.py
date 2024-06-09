from collections import deque


pumps_num = int(input())
pumps = deque()

for _ in range(pumps_num):
    curent_fuel, destination = input().split()
    pumps.append([int(curent_fuel), int(destination)])


start__position = 0
stops = 0

while stops < pumps_num:
    fuel = 0
    for i in range(pumps_num):
        fuel += pumps[i][0]
        destin = pumps[i][1]
        if fuel < destin:
            pumps.rotate(-1)
            start__position += 1
            stops = 0
            break

        fuel -= destin
        stops += 1

print(start__position)