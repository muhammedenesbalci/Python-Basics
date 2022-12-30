print("# Conditional Statements (if - elif - else) ------------------------------")

"""
Evaluated as true or false according to a bool expression.
performing different calculations or actions depending on
is an expression.
"""

list = [1, 2, 3, 4, 5]

deger = input("Enter number : ")
deger = int(deger)

if deger in list:
    print("Yes")
else:
    print("No")

tur = {"one": 1, "two": 2, "three": 3}

letter = input("Enter str")
letter = str(letter)

if letter in tur.keys():
    print("Yes")
else:
    print("No")


sayi1 = 12.0
sayi2 = 20.0

if sayi1 < sayi2:
    print("sayi 1 < sayi2")
elif sayi1 > sayi2:
    print("sayi 1 > sayi2")
else:
    print("sayi 1 == sayi2")



