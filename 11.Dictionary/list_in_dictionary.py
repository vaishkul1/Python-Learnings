# List in Dictionary
"""
anirudh = 250
"""

details = {
    "anirudh": [78, 43, 22],
    "akul": [11, 56, 23],
    "muskan": [98, 91, 3],
}

for k, v in details.items():
    print(f"K = {k}, Type = {type(k)}")
    print(f"V = {v}, Type = {type(v)}")

print("--------")
for k, v in details.items():
    print(f"{k} has scored {sum(v)} marks")

print("--------")

for k, v in details.items():
    total = 0
    for i in v:
        total = total + i
    print(f"{k} has scored {total} marks")
