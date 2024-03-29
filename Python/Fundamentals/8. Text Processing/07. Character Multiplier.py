input_str = input()
str1, str2 = input_str.split()
total_sum = 0
min_len = min(len(str1), len(str2))

for i in range(min_len):
    total_sum += ord(str1[i]) * ord(str2[i])

if len(str1) > len(str2):
    total_sum += sum(ord(char) for char in str1[min_len:])
elif len(str2) > len(str1):
    total_sum += sum(ord(char) for char in str2[min_len:])

print(total_sum)
