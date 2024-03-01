# dictionary = {
#     "name": "Anirudh",
#     "age": 44,
#     "gender": "Male",
#     "marks": [1, 2, 3, 4, 5],
#     "marks1": [1, 2, 3, 4, 5],
#     "adult": True,
#     "married": False,
#     "has_2_legs": True,
#     "xyz": (1, 2, 3),
# }

# print(dictionary)


dictionary = {
    "name": "Anirudh",
    "age": 44,
    "gender": "Male",
    # 1: "abc",
    2: 3,
    3: 3,
    False: False,
    True: True,
    # [1, 2, 3]: "Anirudh",  #mutable object can not be keys
    (1, 2, 3): "Anirudh",  # tuple is immutable hence it can be key
    None: 55,
}

print(dictionary)
