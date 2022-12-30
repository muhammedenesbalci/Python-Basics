print("# Variables------------------------------")

# Integers and floats
a = 5
b = 3.64545

# Variable operations
sum = a + b
sub = a - b
mult = a * b
div = a / b
print(sum, sub, mult, div)

# Various writing
print("Difference : ", a - b)
print("{} + {} = {}".format(a, b, a + b))
print("Multipication : %.4f, Divisioin : %.5f" % (a * b, a / b))

# Change Format
b = int(b)
print(b)

a = float(a)
print(a)

str = "350"
str = int(str)
print(str)

# Strings (we can use for paths or ve can directly enter)
path = "veri" + "\\" + "img" + ".png"

# Variable in strings
a = 18
b = 24

print(f"{a} + {b} = {a + b}")

