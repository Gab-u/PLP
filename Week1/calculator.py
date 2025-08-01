num1 = float(input("Enter your first number: "))
operator = input("Operation: ")
num2 = float(input("Enter your second number: "))

if operator == "+":
    print(f"{num1} {operator} {num2} = {num1 + num2}")
elif operator == "-":
    print(f"{num1} {operator} {num2} = {num1 - num2}")
elif operator == "*":
    print(f"{num1} {operator} {num2} = {num1 * num2}")
elif operator == "/":
    print(f"{num1} {operator} {num2} = {num1 / num2}")
else:
    print(f"{operator} is not a valid operator")