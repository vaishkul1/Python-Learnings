"""   
       *
     * * *
    * * * * *
  * * * * * * *
* * * * * * * * *


"""


for i in range(1, 6):
    for j in range(1, 6 - i):
        print("@", end=" ")
    for k in range(1, (2 * i - 1) + 1):  # if want to start from zero then write 2i-1
        print("*", end=" ")

    print()
