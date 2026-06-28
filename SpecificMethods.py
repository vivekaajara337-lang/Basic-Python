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

#Tuple:
a = ("Vivek","Aajara",10,5,"hi")
print(a.count("V"))
print(a.count(5))

print(len(a))

list = [0,1,2]
print(tuple(list))

print(tuple("Vivek"))

t = (10, 20, 30, 40)
lst = list(t)
lst[2] = 99
t = tuple(lst)
print(t)

# del a
# print(a)

#List:
a = ["aaple","banana","cherry"]
a.append("orange")
print(a)

a.insert(1,"watermelon")
print(a)

a.extend(["Avocado","Blackberry"])
print(a)

b=["Blueberry","Cherry"]
a.extend(b)
print(a)

a.remove("Cherry")
print(a)

a.pop(1)
print(a)

a.pop()
print(a)

del a[0]
print(a)

a.clear()
print(a)

b =a.copy()
print(b)

b=list(a)
print(b)

a.reverse()
print(a)

a.sort()
print(a)

a.sort(reverse=True)
print(a)

# del a
# print(a)

#Dictionary:
a = {
    1:"Vivek",
    2:"Nitin",
    3:"Aditya",
    "year":2026,
    5:5815
}

b = a["year"]
print(b)

b = a.get(3)
print(b)

b = a.keys()
print(b)

b = a.values()
print(b)

b = a.items()
print(b)

a["year"] = 2004
print(a)

a.update({"year":2005})
print(a)

a[5]="Hardik"
print(a)

a.pop("year")
print(a)

a.popitem()
print(a)

a.clear()
print(a)

# del a
# print(a)

#Set:
a={"apple","banana","cherry"}
a.add("orange")
print(a)

b={"pineapple","mango","grape"}
a.update(b)
print(a)

a.remove("pineapple")
print(a)

a.discard("apple")
print(a)

b=a.pop()
print(a)
print(b)

set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}
set3 = set1.union(set2)
Set3 = set3 | set2
print(set3)

