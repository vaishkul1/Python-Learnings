my_list: list[int | str] = [54, 65, 18, 19, 99, 21, 59]
# by index

print(type(my_list))

my_list.append(100)
my_list.append("vai")

print(my_list)

my_list.insert(3, -10)
print(my_list)
my_list.insert(6, -10)
print(my_list)
# if index does not exist then automatically adds at the end
my_list.pop(3)

x = my_list.pop(4)
print(x)


# del
del my_list[0]


# remove by value

my_list.remove(99)
print(my_list)
