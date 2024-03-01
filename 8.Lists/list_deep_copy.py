# deep copy
import copy

my_list = [34, 77, 11, [100, 200, 300], 89, 91, "vai"]
print(my_list)
print(f"{id(my_list) = }")
print(f"{id(my_list[3])= }")
print(id(my_list[1]))

a = copy.deepcopy(my_list)

a = my_list.copy()

a[3][0] = 1  # list in list
print()
print(my_list)
print(a)
print(id(a))
print(id(a[3]))
