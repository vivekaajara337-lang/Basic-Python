import calc
import datetime

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print("Addition:", calc.add(a, b))
print("Subtraction:", calc.subtract(a, b))
print("Multiplication:", calc.multiply(a, b))
print("Division:", calc.divide(a, b))

print("Current Date and Time:", datetime.datetime.now())