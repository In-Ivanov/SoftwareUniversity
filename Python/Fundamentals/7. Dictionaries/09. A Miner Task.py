resource = input()
miner = {}

while resource != "stop":
    if resource not in miner:
        quantity = int(input())
        miner[resource] = quantity
    else:
        quantity = int(input())
        miner[resource] += quantity
    resource = input()

for key, value in miner.items():
    print(f"{key} -> {value}")


