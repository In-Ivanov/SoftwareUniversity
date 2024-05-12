number = float(input())
if number == 0:
    print("zero")
elif number > 0:
    if number < 1:
        print("small positive")
    elif number > 1000000:
        print("large positive")
    else:
        print("positive")
else:
    if abs(number) < 1:
        print("small negative")
    elif abs(number) > 1000000:
        print("large negative")
    else:
        print("negative")
        
'''
#----------------------------------------

num = float(input())
p = 'positive'
n = 'negative'
s = 'small'
l = 'large'

if num > 0:
    if num < 1:
        print(s, p)
    elif num > 1 and num < 1000000:
        print(p)
    else:
        print(l, p)
elif num < 0:
    if num > -1:
        print(s, n)
    elif num < -1 and num > -1000000:
        print(n)
    else:
        print(l, n)
else:
    print('zero')

#-----------------------------------------
'''
