x = (25, 98, 100, 96, 85, 74)
print(id(x))
print(x)
print()

x = list(x)
x.append(100)
# x.append(200)
print(x, id(x))
print()

x = tuple(x)
print(x, id(x))


""" 
x = 10
print(id(x))
print(x)
"""
