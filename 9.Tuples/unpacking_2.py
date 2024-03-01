# also called as splat operator

"""  
name, gender,age, *marks = ["vai", "female",29,89,93,91,99]

print(name)
print(gender)
print(age)
print(marks)
"""

x, *y, z = [100, 250, 300, 450, 700, 890]
print(x)
print(y)
print(z)

print()

*x, y, z = [100, 250, 300, 450, 700, 890]
print(x)
print(y)
print(z)
