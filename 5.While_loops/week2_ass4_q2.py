def pattern(n):
    i = 1
    while i <= n:
        print(i * 10, end=" ")
        i += 1
    print()


pattern(10)


# 2nd approach
def pattern1(n):
    i = 1
    num = 10
    while i <= n:
        print(num, end=" ")
        num = num + 10
        i += 1


pattern1(10)
