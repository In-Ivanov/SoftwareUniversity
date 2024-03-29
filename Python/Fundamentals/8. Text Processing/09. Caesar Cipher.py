text = input()
encrypt = list(map(str, text))
new_version = ""
for i in encrypt:
   new_version += chr(ord(i) + 3)

print(new_version)
