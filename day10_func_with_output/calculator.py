def add(n1,n2):
    return n1+n2

def subtract(n1,n2):
    return n1-n2

def multiply(n1,n2):
    return n1*n2

def divide(n1,n2):
    return n1/n2

operations = {
    "+":add,
    "-":subtract,
    "*":multiply,
    "/":divide,
}

num1 = float(input("what's the first number? "))

value = 0

for symbols in operations:
    print(symbols)

operation_symbol = input("pick an operation from the line above: ")
num2 = float(input("what's the second number? "))
for symbols in operations:
    if operation_symbol == symbols:
        value = operations[symbols](num1,num2)

print(f"{num1} {operation_symbol} {num2} = {value}") 

