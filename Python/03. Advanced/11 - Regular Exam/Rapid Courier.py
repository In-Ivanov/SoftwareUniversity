from collections import deque

packages = [int(x) for x in input().split()]
couriers = deque([int(x) for x in input().split()])


count = 0


while packages and couriers:

    if packages[-1] >= couriers[0]:
        if packages[-1] == couriers[0]:
            count += couriers[0]
            packages.pop()
            couriers.popleft()
        else:
            packages[-1] = packages[-1] - couriers[0]
            count += couriers[0]
            couriers.popleft()

    else:
        couriers[0] = (couriers[0]) - (2 * packages[-1])
        count += packages[-1]
        if couriers[0] <= 0:
            couriers.popleft()
            packages.pop()
        else:
            couriers.append(couriers[0])
            couriers.popleft()
            packages.pop()


if len(packages) > 0:
    print(f"Total weight: {count} kg")
    print(f"Unfortunately, there are no more available couriers to deliver the following packages: {', '.join(map(str, packages))}")
elif len(couriers) > 0:
    print(f"Total weight: {count} kg")
    print(f"Couriers are still on duty: {', '.join(str(p) for p in couriers)} but there are no more packages to deliver.")
else:
    print(f"Total weight: {count} kg")
    print("Congratulations, all packages were delivered successfully by the couriers today.")

