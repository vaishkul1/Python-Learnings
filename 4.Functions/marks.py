def marks(physics: int, chemistry: int, english: int, science: int, hindi: int):
    total = physics + chemistry + english + science + hindi
    per = total / 500 * 100
    print(f"your total marks= {total}")
    print(f"your percentage= {per:.2f}")


# marks(67,32,12,99)

marks(english=10, hindi=99, physics=67, chemistry=67, science=91)  # named arguments
marks(99, 67, hindi=67, science=67, english=91)  # named arguments
# marks(hindi=67, science=67, english=91,99, 67)       #not allowed
