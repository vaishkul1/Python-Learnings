"""   
original_list = [2, 3.75, 0.04, 59.345, 6, 7.777, 8, 9]
only_int = [i for i in original_list if type(i) == int]
only_float = [i for i in original_list if type(i) == float]
a = 5

if type(a) == int:
    print("yes")
else:
    print("no")


    
"""


def checkDiv(n: int) -> bool:
    if n % 2 == 0 and n % 3 == 0:
        return True
    else:
        return False


my_list = [i for i in range(1, 51) if checkDiv(i) == True]
print(my_list)


# my_list = [i for i in range(1,51) if i%2 == 0 and i%3 ==0]


def prime(n: int) -> bool:
    fact = 0
    for i in range(1, n + 1):
        if n % i == 0:
            fact += 1
    if fact == 2:
        return True
    else:
        return False


a = [i for i in range(1, 51) if prime(i) == True]
print(a)
