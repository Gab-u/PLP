def add(num1, num2):
    return num1 + num2
def sub(num1, num2):
    return num1 - num2
def mul(num1, num2):
    return num1 * num2
def div(num1, num2):
    return num1 / num2

operators = {"+": add, "-": sub, "*": mul, "/": div}

num1 = float(input("Enter your first number: "))
operator = input("Operation: ")
num2 = float(input("Enter your second number: "))

result = operators[operator](num1, num2)
print(f"{num1} {operator} {num2} = {result}")