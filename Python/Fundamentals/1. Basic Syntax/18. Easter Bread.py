budget = float(input())
kg_flour = float(input())
pack_eggs = kg_flour * 0.75
milk = (kg_flour * 1.25) / 4

one_loaf = kg_flour + pack_eggs + milk

loaves = 0
colored_eggs = 0

while budget >= one_loaf:
    loaves += 1
    budget -= one_loaf
    colored_eggs += 3
    if loaves % 3 == 0:
        colored_eggs -= loaves - 2

print(f"You made {loaves} loaves of Easter bread! Now you have {colored_eggs} eggs "
      f"and {budget:.2f}BGN left.")