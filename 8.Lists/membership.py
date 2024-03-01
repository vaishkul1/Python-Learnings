# membership operator (IN/ NOT IN)
my_list: list[int] = [54, 99, 18, 19, 99, 21, 59]


x = my_list.count(99)
print(x)


search_number = 99

if search_number in my_list:
    print("yes")
else:
    print("NO")


if my_list.count(search_number) > 0:
    print("yes")
else:
    print("no")
