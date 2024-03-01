# default /required parameters. all required on left side, all default on right side
def marks(physics, chemistry, english=0, science=0, hindi=0):
    total = physics + chemistry + english + science + hindi
    per = total / 500 * 100
    print(f"your total marks= {total}")
    print(f"your percentage= {per:.2f}")


# marks(56,11,89,78,99)
# marks(english=99,hindi=45,chemistry=11,science=34,physics=89)
marks(56, 12, hindi=90)
