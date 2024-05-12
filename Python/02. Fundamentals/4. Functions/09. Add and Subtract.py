
def sum_numbers(num1, num2):
    return num1 + num2


def subtract(result, num3):
    return result - num3


def add_and_subtract(num1, num2, num3):
    result = sum_numbers(num1, num2)
    return subtract(result, num3)


num1, num2, num3 = int(input()), int(input()), int(input())
print(add_and_subtract(num1, num2, num3))


"""


def sum_numbers(a, b):
    return a + b


def subtract(c, d):
    return sum_numbers(num_1, num_2) - d


num_1 = int(input())
num_2 = int(input())
num_3 = int(input())
result = subtract(sum_numbers(num_1, num_2), num_3)

print(result)


"""









