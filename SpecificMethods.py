#String:
a = "Vivek"
print(a.find("ek"))

print(a.replace("ek", "ka"))

print(a.upper())

print(a.lower())

b= "Nitin"
print(b.count("i"))
print(a.count("v"))

print(b.islower())

print(b.isupper())

print(b.isnumeric())

print(b.isalpha())

print(a.isprintable())

#Tuple
a = ("Vivek","Aajara",10,5,"hi")
print(a.count("V"))
print(a.count(5))

print(len(a))

list = [0,1,2]
print(tuple(list))

print(tuple("Vivek"))

# t = (10, 20, 30, 40)
# lst = list(t)
# lst[2] = 99
# t = tuple(lst)
# print(t)

del a
print(a)

#List
a = ["aaple","banana","cherry"]
a.append("orange")
print(a)

