s1 = input()
s2 = input()
st = input()
um = 0
for a in st:
    if ord(s1) < ord(a) < ord(s2):
        um += ord(a)
print(um)

