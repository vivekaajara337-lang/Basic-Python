#Take 5 numbers as input and find out min and max form that.
num1 = int(input("Enter a number: "))
num2 = int(input("Enter another number: "))
num3 = int(input("Enter another number: "))
num4 = int(input("Enter another number: "))
num5 = int(input("Enter another number: "))

minimum = min(num1, num2, num3, num4)
maximum = max(num1, num2, num3, num4)

print("The minimum number is ", minimum)
print("The maximum number is ", maximum)