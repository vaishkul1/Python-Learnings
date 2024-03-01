# 1 3 6 8 11 13 16 18 21 23

i = 0
num = 1

while i < 10:
    print(num, end=" ")
    if i % 2 == 0:
        num += 2
    else:
        num += 3
    i += 1
