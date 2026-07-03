#Singe Inheritance
class A:
    def __init__(self, something):
        print("Base Class A")
        self.something = something

class B(A):
    def __init__(self, something):
        A.__init__(self, something)
        print(" Child Class B")
        self.something = something

obj = B("")

#Multiple Inheritance
class A:
    def __init__(self, something):
        print("Base Class A")
        self.something = something

class B:
    def __init__(self, something):
        A.__init__(self, something)
        print(" Child Class of A")
        self.something = something

class C(A,B):
    def __init__(self, something):
        A.__init__(self, something)
        B.__init__(self, something)
        print(" Child Class of B")


obj = C("")

##Multilevel Inheritance
class A:
    def __init__(self, something):
        print("Base Class A")
        self.something = something


class B(A):
    def __init__(self, something):
        A.__init__(self, something)
        print(" Child Class of A")
        self.something = something


class C(B):
    def __init__(self, something):
        B.__init__(self, something)
        print(" Child Class of B")
        self.something = something

obj = C("")

#Hierarchical Inheritance
class emp():
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

class emp1(emp):
    def __init__(self, name, salary):
        emp.__init__(self, name, salary)
        print(" Child Class of emp1")
        self.salary = salary

class emp2(emp):
    def __init__(self, name, salary):
        emp.__init__(self, name, salary)
        print(" Child Class of emp2")
        self.salary = salary

e1 = emp1("Vivek", "14000")
e2 = emp2("Nitin", "24000")

print(e1.name, e1.salary)
print(e2.name, e2.salary)
