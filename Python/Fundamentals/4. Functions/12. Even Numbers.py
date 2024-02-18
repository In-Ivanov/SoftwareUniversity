'''
def even(n):
    return n % 2 == 0


nums = map(int, input().split(" "))

filtered_nums = filter(even, nums)


print(list(filtered_nums))
'''







filtered_nums = filter(lambda iop: iop % 3 == 0, (1, 2, 3, 4))


print(list(filtered_nums))