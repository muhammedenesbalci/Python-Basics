print("# Tuples ------------------------------------")

"""
- Not changable(we can't change element, we can just add element) and sorted a list variation
"""

tuple_variable = (1, 2, 3, 4, 5, 6, 6, 6)

print(tuple_variable)

# Specific element
print(tuple_variable[2])

# certain range
print(tuple_variable[1:6:2])

# Counting an variable
print(tuple_variable.count(6))

# We can use tuple to decomposition
x, y, z = (1, 2, 3)
print(x, y, z)
