""" 
truthy
falsy value

int -> anything which is not zero is truthy
int -> 0 falsy

float -> anythin truthy
float -> 0.0 falsy

string -> "vai" "1" " " truthy
string -> "" falsy

boolean -> True truthy
boolesn -> false falsy
"""

if 5:
    print("yes")
else:
    print("no")

if 0:
    print("yes")
else:
    print("no")


name = input("enter yout name= ")
if name:
    print(f"greetings to {name}")
else:
    print("no name")


""" 
old method 

if name != "":
    print(f"greetings to{name}")
else:
    print("no name")
"""
