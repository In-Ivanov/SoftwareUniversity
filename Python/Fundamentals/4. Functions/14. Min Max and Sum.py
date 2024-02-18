def mininuma(a):
    return min(a)


def maximuma(a):
    return max(a)


def sumata(a):
    return sum(a)


numbers = list(map(int, input().split(" ")))
result1 = int(mininuma(numbers))
result2 = int(maximuma(numbers))
result3 = sumata(numbers)
print(f"The minimum number is {result1}")
print(f"The maximum number is {result2}")
print(f"The sum number is: {result3}")
