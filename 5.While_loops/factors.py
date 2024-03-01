def printFactors(num: int):
    i = 1
    count = 0
    while i <= num:
        if num % i == 0:
            # print(i, end=" ")    #if que is to print factors
            count += 1  # if que is to count the factors
        i += 1
    print(f"total factors are{count}")
    print()


def checkprime(num: int):
    i = 1
    count = 0
    while i <= num:
        if num % i == 0:
            count += 1
        i += 1

    if count == 2:
        print("prime no")
    else:
        print("not prime")
    print(f"total factors are {count}")
    print()


printFactors(25)
checkprime(4)
