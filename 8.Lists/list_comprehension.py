# a = [i for i in range(1, 5000001)]
# a = ["odd" for i in range(1, 11)]
# a = [f"odd{i}" for i in range(1, 11)]
a = [i % 2 == 0 for i in range(1, 11)]


# a = []
# for i in range(1, 1000001):
#     a.append(i)

print(a)
