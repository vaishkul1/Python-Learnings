""" 
enter a num = 5
enter a num = 10
enter a num = 7
enter a num = 0
stop the loop when got 0 
print total of all the things we got in input

"""
total = 0
while True:
    n = int(input("enter a number= "))
    total += n
    if n == 0:
        break

print(total)
