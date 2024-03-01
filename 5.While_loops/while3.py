"""ask a number from user print 1 to n """

"""  
i = 1
while i <= N:
    print(i, end=" ")
    i += 1
"""


def print1toN(n):
    i = 1
    while i <= n:
        print(i, end=" ")
        i += 1


N = int(input("Enter a number= "))
print1toN(19)
print1toN(N)
