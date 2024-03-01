"""  
1
12
123
1234
12345
"""

for i in range(1, 6):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()

print()

for i in range(1, 6):
    for j in range(1, i + 1):
        print(i, end=" ")
    print()

print()


def pattern(n):
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            print(j, end=" ")
        print()


pattern(9)
