detail = {
    "name": "Anirudh",
    "age": 55,
    "gender": "Male",
}

# Iterating
print(detail.keys())

print("2-----------")

for i in detail.keys():
    print(i, detail[i])  # to print key and value

print("3-----------")


for i in detail.values():
    print(i)  # only values

print("4-----------")

print(detail.items)
print("5-----------")

for k, v in detail.items():
    # print(f"Key = {k} and Value = {v}")
    print(f"{k}={v}")
