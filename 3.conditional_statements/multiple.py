"""
ask a no from userr
if divisible by 5 and 6 then yes otherwise no   
"""

num1 = int(input("Enter a number= "))

if num1 % 5 == 0 and num1 % 6 == 0:
    print("YES!")
else:
    print("NO")
