maths = int(input("enter maths marks= "))
history = int(input("enter history marks= "))
english = int(input("enter english marks= "))
geography = int(input("enter geography marks= "))
marathi = int(input("enter marathi marks= "))

total = maths + history + english + geography + marathi

percentage = (total / 500) * 100

percentage = round(percentage, 2)
