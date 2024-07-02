n = int(input())


def print_upper_part(size):
    for row in range(1, size+1):
        print(" " * (size - row), "* " * row)



def _print_lower_part(size):
    for row in range(size - 1, 0, -1):
        print(" " * (size - row), "* " * row)


print_upper_part(n)