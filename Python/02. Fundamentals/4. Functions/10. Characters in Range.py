'''
def chars_range(first_char, second_char):
    result = ""

    for i in range(ord(first_char) + 1, ord(second_char)):
        result += chr(i) + " "

    return result


char1 = input()
char2 = input()
print(chars_range(char1, char2))

'''












def char_range(ch1, ch2):
    result = ""
    for i in range(ord(ch1) + 1, ord(ch2)):
        result += chr(i) + " "
    return result


note1 = input()
note2 = input()
string = char_range(note1, note2)
print(string)
