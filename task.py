# def format_name(f_name, l_name):
#     f_name.title()
#     l_name.title()
#     return f"{f_name} {l_name}".title()

# formated_string = format_name("rYaN", "PUZO")
# print(formated_string)

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
    "/": divide
}

num1 = float(input("Enter first number: "))
for symbol in operations:
    print(symbol)
operation_symbol = input("Type mathematical operator: ")
num2 = float(input("Enter second number: "))

print(operations[operation_symbol](num1, num2))