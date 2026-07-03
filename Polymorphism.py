#Runtime Polymorphism
def add(a, b, c = 0):
    return a + b + c

print(add(1, 2))
print(add(1, 2, 3))

#Compile time Polymorphism
class A:
    def sum(self,a,b):
        return a+b

class B(A):
    def sum(self,a,b):
        return a+b

obj1 = A()
obj2 = B()

print("ans:", obj1.sum(4,5))
print("ans:", obj2.sum(4,6))
