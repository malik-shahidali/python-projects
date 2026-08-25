num1 = int(input("enter a number: "))
num2 = int(input("enter another number: "))
operator = input("enter an operator (+, -, *, /): ")

if operator == "+":
    print("answer:", num1 + num2)
elif operator == "-":
    print("answer:", num1 - num2)
elif operator == "*":
    print("answer:", num1 * num2)
elif operator == "/":
    print("answer:", num1 / num2)
else:
    print("invalid operator")