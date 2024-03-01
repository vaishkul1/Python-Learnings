"""  
n1 and n2 
calculate total of all nos divisible
 by 3 and 6 between n1 and n2
"""


def calsum(n1: int, n2: int):
    i = n1
    total = 0
    while i <= n2:
        if i % 3 == 0 and i % 6 == 0:
            total = total + i
        i += 1
    print(total)


calsum(1, 20)
