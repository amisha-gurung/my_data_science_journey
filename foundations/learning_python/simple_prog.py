#a simple program that: takes two numbers as input from the user, performs addition subtraction, multiplication and division, prints the result for each operation
# user inputs:
print('Enter two numbers\n')
a = input("Enter a: ")
b = input("Enter b: ")

a = float(a)
b = float(b)

# calculations
add = a + b
sub = a - b
mul = a * b
div = a / b if b != 0 else "Undefined (division by zero)"

print('Addititon: ', add)
print("Subtraction: ", sub)
print("Multiplication: ", mul)
print("Division: ", div)
