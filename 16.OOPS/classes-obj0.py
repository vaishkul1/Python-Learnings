# this is not correct way there are some problems in it


class Student:
    name = ""
    age = 0
    gender = "-"
    # phone    #althogh we havent made the attribute. it is automatically created for that instance

    def display(self):
        print(f"My name is {self.name}")
        print(f"My age is {self.age}")
        print(f"My gender is {self.gender}")

    def setInfo(self):
        self.name = input("Enter name = ")
        self.age = int(input("Enter age = "))
        self.gender = input("Enter gender = ")
        self.phone = input("Enter phone = ")


# s1 i object
s1 = Student()
# s1.name = "vai"  # to avoid this line we can make another method setinfo in which it will take info from user.
s1.display()
s1.setInfo()


# the method display is used to avoid the below three print statments

"""  
print(s1.name)
print(s1.age)
print(s1.gender)
"""


"""   

# s2 is object
s2 = Student()
print(s2.name)
s2.age = 9
print(s2.age)
print(s2.gender)


"""
