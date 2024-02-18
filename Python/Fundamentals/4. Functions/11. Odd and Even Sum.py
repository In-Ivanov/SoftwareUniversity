
'''
def odd_even_sum(number):
    odd_sum = 0
    even_sum = 0

    for digit in str(number):

        if int(digit) % 2 == 0:
            even_sum += int(digit)
        else:
            odd_sum += int(digit)

    return f"Odd sum = {odd_sum}, Even sum = {even_sum}"


number = int(input())
print(odd_even_sum(number))





'''







def odd_even(a):
    odd = 0
    even = 0
    for i in range(len(a)):
        num = int(a[i])
        if num % 2 == 0:
            even += num
        else:
            odd += num
    return f"Odd sum = {odd}, Even sum = {even}"


number = input()
print(odd_even(number))











