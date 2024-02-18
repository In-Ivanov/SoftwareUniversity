def calculations(a, b, oper):
    result = None
    if oper == "multiply":
        result = a * b
    elif oper == "divide":
        result = int(a / b)
    elif oper == "add":
        result = a + b
    elif oper == "subtract":
        result = a - b
    return result


operator = input()
number_one = int(input())
number_two = int(input())


result = calculations(number_one, number_two, operator)
print(result)

