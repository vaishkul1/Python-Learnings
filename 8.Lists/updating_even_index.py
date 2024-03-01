# using function

# all at even index should be zero
from typing import List


def evenIndexUpdate(lst: List[int]) -> None:
    for i in range(0, len(lst)):
        if i % 2 == 0:
            lst[i] = 0


my_list = [54, 43, 19, 85, 11, 94, 32]
evenIndexUpdate(my_list)
print(my_list)


# numbers which are even


def evenNumberUpdate(lst: List[int]) -> None:
    for i in range(0, len(lst)):
        if lst[i] % 2 == 0:
            lst[i] = 0


my_list = [54, 43, 19, 85, 11, 94, 32]

evenNumberUpdate(my_list)
print(my_list)
