""" 
control statements (only comes in loops)
1. break 
2. continue
"""


i = 1
while i <= 10:
    if i == 5:
        continue  # this statement continues the while loop but doesnt run anything that is below it
    print(i)
    i += 1
# for above ans: continuous loop
j = 1
while j <= 10:
    j += 1
    if j == 5:
        continue  # this statement continues the while loop but doesnt run anything that is below it
    print(i)
