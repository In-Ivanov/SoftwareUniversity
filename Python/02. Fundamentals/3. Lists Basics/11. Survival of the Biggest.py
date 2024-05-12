numbers = list(map(int, input().split()))
remover = [numbers.remove(min(numbers)) for _ in range(int(input()))]

numbers_ = ", ".join(map(str, numbers))
print(numbers_)