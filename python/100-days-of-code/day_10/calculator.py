import os
from art import logo

def add(n1, n2):
  return n1 + n2

def subtract(n1, n2):
  return n1 - n2

def multiply(n1, n2):
  return n1 * n2

def divide(n1, n2):
  return n1 / n2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}

def calculator():
    # show the calculator logo
    print(logo)

    num1 = float(input("What's the first number?: "))

    for operator in operations:
        print(operator)

    should_continue = True
    while should_continue == True:
        operation_symbol = input("Pick an operation: ")

        num2 = float(input("What's the next number?: "))

        function = operations[operation_symbol]
        answer = round(function(num1, num2), 2)

        print(f"{num1} {operation_symbol} {num2} = {answer}")

        if input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ") == 'y':
            num1 = answer

        else:
            should_continue = False
            os.system("clear")
            calculator()

calculator()

