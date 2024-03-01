my_string = "pyTHon is Goo*^^d"


# swap the cases from upper to lower but dont change symbols and numbers. they should be as it is

result = ""

for i in my_string:
    if i.isupper():
        result += i.lower()
    elif i.islower():
        result += i.upper()
    else:
        result += i

print(result)
