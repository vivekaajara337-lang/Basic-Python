class Calculator:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2
        
    def add(self):
        return self.num1 + self.num2

    def subtract(self):
        return self.num1 - self.num2

    def multiply(self):
        return self.num1 * self.num2

    def divide(self):
        if self.num2 == 0:
            return "Division by zero is not allowed."
        return self.num1 / self.num2


num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

calc = Calculator(num1, num2)

print("\nChoose Operation")
print("1.Addition")
print("2.Subtraction")
print("3.Multiplication")
print("4.Division")

choice = int(input("Enter your choice: "))

if choice == 1:
    print("Ans =", calc.add())
elif choice == 2:
    print("Ans =", calc.subtract())
elif choice == 3:
    print("Ans =", calc.multiply())
elif choice == 4:
    print("Ans =", calc.divide())
else:
    print("Invalid choice.")
