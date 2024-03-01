"""  
make a function that accepts 2 integer as an argument(n1,n2)
n1 -> n2 
print prime number 
printPrime(2,10 )

print(50,60)
"""


def printPrime(n1, n2):
    for num in range(n1, n2 + 1):
        factor = 0
        for i in range(1, num + 1):
            if num % i == 0:
                factor += 1
        if factor == 2:
            print(num)


printPrime(3, 13)
