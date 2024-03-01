"""  
my_string = "python Is a gOOd lanGuAGe"
x = my_string.swapcase()
print(x)

"""

a = "python"

a += "z"
print(id(a))
a += "x"
print(id(a))
a += "y"
print(id(a))
print(a)


"""   
keep asking characters from user
until user types quit
enter character = 
enter character = 
enter character = 
enter character = 
print the word

"""

my_string = ""
while True:
    char = input("Enter character= ")
    if char == "quit":
        break
    my_string += char

print(my_string)
