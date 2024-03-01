"""
ask a no
if no divisible by 3 > FOO
if no divisible by 5 > BAR
if no divisible by 3 and 5 > fooBAR
nothing FOOFOOBARBAR
 """


num1 = int(input("give one number= "))

if num1 % 3 == 0 and num1 % 5 == 0:
    print("FOOBAR")
elif num1 % 3 == 0:
    print("FOO")
elif num1 % 5 == 0:
    print("BAR")
else:
    print("FOOFOOBARBAR")
