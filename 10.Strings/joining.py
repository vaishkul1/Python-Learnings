# joining
# list to string
a = ["python", "is", "good", "language"]
b = [1, 5, 7, 11]
c = ["python", "is", "good", "language", True, 99]

x = " ".join(i for i in a)
y = " | ".join(i for i in a)
z = " ".join(str(i) for i in b)  # joining can onli be done if they are str not for int
z1 = " ".join(str(i) for i in c)  # joining can onli be done if they are str not for int

print(x)
print(y)
print(z)
print(z1)
