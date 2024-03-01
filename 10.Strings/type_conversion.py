string = "1234a"

x = list(string)
print(x)

x[0] = "Z"
print(x)

print(x, type(x))

r = "".join(i for i in x)
# r = "".join(x)     #same as above
r = "".join(i for i in x[::-1])  # if want reverse
print(r)
print(type(r))
