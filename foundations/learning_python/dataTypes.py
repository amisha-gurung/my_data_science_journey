#Understanding Data types and Type conversion
age = input("Enter age: ")
height = input("Enter height in meter: ")
name = input("Enter name: ")
age= int(age)
height = float(height)
print(type(age))
print(type(height))
print(type(name))
age_inmonth = age *12
print(f"Hi {name}, you are {age} years old, {height}m tall, and that's {age_inmonth} months!")