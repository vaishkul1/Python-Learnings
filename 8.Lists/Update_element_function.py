from typing import List

"""  
pass by value


def xyz(a: int) -> None:
    a[0] = 100


a = 1
xyz(a)
print(a)

"""


# pass by reference
def xyz(a: List) -> None:
    a[0] = 100


a: List = [43, 54, 65, 32, 111]
xyz(a)
print(a)
