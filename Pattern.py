#pattern:
#1.1
#  11
#  111
#  1111
#  11111
for i in range(1, 6):
    print("1" * i)

print()

#2.A
#  AB
#  ABC
#  ABCD
#  ABCDE
for i in range(1, 6):
    print("".join(chr(64 + j) for j in range(1, i + 1)))
print("\n")

#3.1
#  12
#  345
#  6789
num = 1
for i in range(1, 5):
    for j in range(i):
        print(num, end="")
        num += 1
    print()
print("\n")

#4.     *
#     * * *
#   * * * * *
# * * * * * * *
n = 4
for i in range(1, n + 1):
    spaces = "  " * (n - i)
    stars = "* " * (2 * i - 1)
    print(spaces + stars)
print("\n")