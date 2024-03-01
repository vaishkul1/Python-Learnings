# ask user check if odd or even
# ternary operators
def check(num: int) -> str:
    # print("even") if num%2 == 0 else print("odd")
    # if you want to use multiple statements then following code
    if num % 2 == 0:
        return "even"
    else:
        return "odd"

    # if single statement return then use following
    # return "even" if num %2 ==0 else 'odd'


x = check(10)
print(x)
