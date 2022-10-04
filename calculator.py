def addition(n1, n2):
    return n1 + n2


def subtraction(n1, n2):
    return n1 - n2


def multiplication(n1, n2):
    return n1 * n2


def division(n1, n2):
    return n1 / n2


while True:

    operation = int(input(''' 
    please select the type operation that you want to perform
    1 + for addition
    2 - for subtraction
    3 * for multiplication
    4 / for division
    5 Exit
    '''))
    if operation == 1:
        num1 = int(input("Enter the first number  : "))
        num2 = int(input("Enter the second number : "))

        print(f"{num1} + {num2} = ", addition(num1, num2))

    elif operation == 2:

        num1 = int(input("Enter the first number  : "))
        num2 = int(input("Enter the second number : "))

        print(f"{num1} - {num2} = ", subtraction(num1, num2))

    elif operation == 3:
        num1 = int(input("Enter the first number  : "))
        num2 = int(input("Enter the second number : "))

        print(f"{num1} * {num2} = ", multiplication(num1, num2))

    elif operation == 4:

        num1 = int(input("Enter the first number  : "))
        num2 = int(input("Enter the second number : "))

        if num2 == 0:
            print("cannot divide by zero")
        else:
            print(f"{num1} / {num2} = ", division(num1, num2))

    elif operation == 5:
        break
    else:
        print("Enter a valid operator, please run the program again.")
