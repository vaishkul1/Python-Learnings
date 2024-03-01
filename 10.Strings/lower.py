my_string = input("Enter a string= ")

# how many lower:

count = 0
for ch in my_string:
    if ch.islower():
        count += 1

print(count)


count = 0
for ch in my_string:
    ascii = ord(ch)
    if ascii >= 97 and ascii <= 122:
        count += 1

print(count)


"""
to check if the given string is completely lower
if my_string.islower():
    print("yes")
else:
    print("no")

"""
