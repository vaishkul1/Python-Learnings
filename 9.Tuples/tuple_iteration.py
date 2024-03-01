x = (25, 98, 100, 96, 85, 74)

# by index
for i in range(0, len(x)):
    print(x[i])

# by value
for i in x:
    print(i)

for index, value in enumerate(x):
    print(index, value)
