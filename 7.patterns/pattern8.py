"""  
        *
      * *
    * * *
  * * * *
* * * * *
"""

"""  
for i in range(1, 6):
    for j in range(1, 6 - i):
        print(" ", end=" ")
    for k in range(1, i + 1):
        print("*", end=" ")
    print()


"""


def pattern(n):
    for i in range(1, n + 1):
        for j in range(1, 6 - i):
            print(" ", end=" ")
        for k in range(1, i + 1):
            print("*", end=" ")
        print()


x = pattern(5)
print(x)
