word = input()
reverse_word = ""
for i in range(len(word) - 1, -1, -1):
    reverse_word += word[i]
print(reverse_word)

'''
#--------------------------------

txt = input()[::-1]
print(txt)

#----------------------------------

x = input()
y = ''
for i in x:
    y = i + y
print(y)

#-------------------------------------

x = input()

x_reversed = ''
index = len(x) - 1

while index >= 0:
    x_reversed = x_reversed + x[index]
    index = index - 1

print(x_reversed)

#-------------------------------------

x = list(input())
x.reverse()
x_reversed = ''.join(x)
print(x_reversed)

#--------------------------------------
'''
