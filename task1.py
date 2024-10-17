def addition(n1, n2):
    return n1 + n2
def subtraction(n1, n2):
    return n1 - n2
def multiplication(n1, n2):
    return n1 * n2
def division(n1, n2):
    return n1 / n2

num1 = int(input("Enter a number: "))
num2 = int(input("Enter a number: "))
operation = input("Chose an operation(addition, subtraction, multiplication, division): ")

if operation == "addition":
    print(addition(num1, num2))
elif operation == "subtraction":
    print(subtraction(num1, num2))
elif operation == "multiplication":
    print(multiplication(num1, num2))
elif operation == "division":
    print(division(num1, num2))
else:
    print ("error")