""" 
make a function named printMtoN
printMtoN(n1,n2) | n1<n2

printMtoN(1,7)
1,2,3,4,5,6,7
"""


def printMtoN(n1: int, n2: int) -> None:  # wrong way avaid
    while n1 <= n2:
        print(n1, end=" ")
        n1 += 1
    print()


def newWay(n1, n2):
    if n1 > n2:
        return
    i = n1
    while i < +n2:
        print(i, end=" ")
        i += 1

    print()


printMtoN(2, 5)
