# iteration by index


lst = [67, 54, 11, 99, 98, 432, 432, "vai", True, 55.556]

x = len(lst)

print(x)
# by index
for i in range(0, x):
    print(lst[i], end=" ")

print()
for i in range(len(lst)):
    print(lst[i], end=" ")

print()
for i in range(len(lst), -1, -1):
    print(i, end=" ")
print()
for i in range(len(lst) - 1, -1, -1):
    print(lst[i], end=" ")

print()
for i in range(-1, -len(lst) - 1, -1):
    print(lst[i], end=" ")
print()

# by value
my_list = [12, 13, 13, 33, 56]
for i in my_list:
    print(i, end=" ")


for i in my_list:
    if i % 2 == 0:
        print(i, end=" ")


print(list(enumerate(my_list)))


for i, j in enumerate(my_list):
    print(f"index = {i}, value= {j}")
