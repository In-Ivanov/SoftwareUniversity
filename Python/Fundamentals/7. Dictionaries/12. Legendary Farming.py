key_materials = {"shards": 0, "fragments": 0, "motes": 0}
items = input().split()
while True:
    flag = False
    for i in range(0, len(items), 2):
        quantity = int(items[i])
        material = items[i + 1].lower()

        if material in key_materials:
            key_materials[material] += quantity

            if key_materials[material] >= 250:
                if material == "shards":
                    print("Shadowmourne obtained!")
                elif material == "fragments":
                    print("Valanyr obtained!")
                elif material == "motes":
                    print("Dragonwrath obtained!")
                key_materials[material] -= 250
                for (material, quantity) in key_materials.items():
                    print(f"{material}: {quantity}")
                flag = True
                break
        if material not in key_materials:
            key_materials[material] = 0
            key_materials[material] += quantity
        if flag == True:
            break
    if flag == True:
        break
    items = input().split()












