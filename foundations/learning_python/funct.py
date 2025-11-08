# write a function add_numbers that: accepts two numbers as parameters, returns their sum, call the function with different input and print the result
def add_numbers(num1, num2):
    return num1 + num2

a = input("Enter first number: ")
b = input("Enter second number: ")

result = add_numbers(float(a), float(b))
print("The sum is: ",result)