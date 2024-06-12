n = int(input())

name = set()

for _ in range(n):
    names = input()
    name.add(names)
print(*name, sep='\n')


