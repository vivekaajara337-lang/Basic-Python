class A:
    a = 10
    b = 50

obj = A()
print(obj.a)

class B:
    def __init__(self,a,b):
        self.a = a
        self.b = b

obj = B(a=10,b=50)
print(obj.a)
print(obj.b)

class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def display(self):
        print("Name:",self.name)
        print("Age:",self.age)
p1 = Person("Adity",14)
p2 = Person("Vivek",22)
p3 = Person("Nitin",23)
p1.display()
p2.display()
p3.display()

