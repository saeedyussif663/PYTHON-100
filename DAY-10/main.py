def add(n1, n2):
    return n1 + n2

def sub(n1, n2):
    return n1 - n2

def mul(n1, n2):
    return n1 * n2

def div(n1, n2):
    return n1 / n2

operations = {
    "+": add,
    "-": sub,
    "*": mul,
    "/": div,
}

def calculator():
    num1 = float(input("What is the first number? "))
    for symbol in operations:
        print(symbol)

    should_continue = True

    while should_continue:
        operation_symbol = input("pick an operation from the line above: ")
        num2 = float(input("What is the next number? "))
        func = operations[operation_symbol]
        answer = func(num1, num2)
        print(f"{num1} {operation_symbol} {num2} = {answer}")
        if input(f"Type 'y' to continue or calculating with the {answer}, or type n to start a new calculation: ") == "y":
            num1 = answer
        else:
            should_continue = False
            calculator()

calculator()