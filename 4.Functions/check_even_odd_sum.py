"""
ask 2 nos
calculate total
check total odd or even

    """


def total(num1: int, num2: int) -> int:
    return num1 + num2


def checkEvenOdd(num: int) -> None:
    if num % 2 == 0:
        print("Even")

    else:
        print("Odd")


num1: int = int(input("Enter a number "))

num2: int = int(input("Enter a number "))

t = total(num1, num2)

print(t)

checkEvenOdd(t)
