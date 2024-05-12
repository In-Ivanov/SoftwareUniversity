import re

string = input()
emojis = []
em = []
pattern = r"(\:{2}|\*{2})([A-Z][a-z]{2,})\1"
matches = re.finditer(pattern, string)
cool = [int(x.group()) for x in re.finditer(r"\d", string)]
tr = 1
for c in cool:
    tr *= c
for match in matches:
    emojis.append(match.group())
    em.append(match.group(2))

print(f"Cool threshold: {tr}")
print(f"{len(emojis)} emojis found in the text. The cool ones are:")

for l in range(len(em)):
    p = 0
    for i in em[l]:
        p += ord(i)
    if p >= tr:
        print(emojis[l])
        p = 0
    else:
        continue
