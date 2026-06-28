#Arithmetic Operators:
a=3
b=5
add=a+b
print(add)

sub=a-b
print(sub)

mult=a*b
print(mult)

div=a/b
print(div)

mod=a%b
print(mod)

exponent=a**b
print(exponent)

floor=a//b
print(floor)

#Assignment Operators:
a=10
print(a)

a+=5
print(a)

a-=3
print(a)

a*=3
print(a)

a/=3
print(a)

a%=3
print(a)

a**=3
print(a)

a//=3
print(a)

#Comparison Operators:
a = 10
b = 5

print("a == b :", a == b)
print("a != b :", a != b)
print("a <> b  :", a > b)
print("a > b  :", a < b)
print("a < b :", a >= b)
print("a >= b :", a >= b)
print("a <= b :", a <= b)

#Logical Operators:
a = 10
b = 5

print(a > 5 and b < 10)
print(a > 15 or b < 10)
print(not(a > 5))

#Identity Operators:
a = [1, 2, 3]
b = a
c = [1, 2, 3]
print(a is b)
print(a is c)

print(a is not b)
print(a is not c)

#Membership Operators:
a = ["apple", "banana", "mango"]

print("apple" in a)
print("grapes" in a)

print("apple" not in a)
print("grapes" not in a)

#Bitwise Operators:
a = 5    # Binary: 0101
b = 3    # Binary: 0011

print(a & b)
print(a | b)
print(a ^ b)
print(~a)
print(a << 1)
print(a >> 1)