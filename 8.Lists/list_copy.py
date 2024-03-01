my_list = [45, 17, 89, 94, "vai", 55.687, 12.225]
print(my_list)
print(id(my_list))


a = my_list
# values copy nhi ki. memory/ address copy kiya hai
print(a)
print(id(a))

a = my_list.copy()  # shallow copy
print(a)
print(id(a))

a[0] = 1000
print("after changing")
print(my_list)
print(a)
