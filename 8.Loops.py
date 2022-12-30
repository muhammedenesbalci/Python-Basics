print("# Loops------------------------------")
"""
- in the transactions we want to make constantly
- Loops are structures used to iterate over an array.
- Arrays: list, tuple, string, dictionary, numpy pandas data types
"""

# For loop
for i in range(1, 11):
    print(i)

for i in ["Muhammed", "Enes", "BALCI"]:
    print(i)

my_tuple = ((1, 2, 3), ("x", "y", "z"))

for x, y, z in my_tuple:
    print(x, y, z)

# While loop
while i < 4:
    print(i)
    i = i + 1

liste = [1, 4, 5, 6, 8, 3, 3, 4, 67]
sinir = len(liste)
