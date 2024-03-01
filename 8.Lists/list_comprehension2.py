# to create a new list
""" 
a = [i for i in range(1, 11)]
print(a)
b = [i + 10 for i in range(1, 11)]
print(b)


c = ["even" if i % 2 == 0 else "odd" for i in range(1, 11)]
print(c)

d = [1 if i % 2 == 0 else 0 for i in range(1, 11)]
print(d)


e = [i for i in range(1, 11) if i % 2 == 0]
print(e)

"""

# if no odd then aquare if even then cube


a = [i**2 if i % 2 != 0 else i**3 for i in range(1, 21)]
print(a)
