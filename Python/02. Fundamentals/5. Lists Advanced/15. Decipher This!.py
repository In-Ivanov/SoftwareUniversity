secret_message = input().split(" ")
decipher = []
number_for_char = ""
decipher_list = []

for i in secret_message:
    for n in i:
        if n.isdigit():
            number_for_char += n
        else:
            decipher.append(n)
    note = chr(int(number_for_char))
    decipher.insert(0, note)
    note2 = decipher[1]
    note_end = decipher[-1]
    decipher[1] = note_end
    decipher[-1] = note2
    decipher_list.extend(decipher)
    decipher_list.extend(" ")
    decipher = []
    number_for_char = ""

print("".join(decipher_list))
