x = input("enter a number= ")

# if digit then convert to int else print invalid

if x.isdigit():
    x = int(x)
    print(x, type(x))
else:
    print("INVALID")
