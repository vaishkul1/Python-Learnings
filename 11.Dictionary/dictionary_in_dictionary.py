student_details = {
    "anirudh": {
        "age": 66,
        "gender": "Male",
        "address": "Surat",
        "phone": 100,
    },
    "nihar": {
        "phone": 3213421,
        "gender": "Male",
        "address": "Delhi",
        "age": 16,
    },
}


print(student_details["anirudh"]["address"])
print(student_details["anirudh"])
print()
print("--------------------")
print()

for name, details in student_details.items():
    print(name)

print()
print("-----------------")
print()
for name, details in student_details.items():
    print(details)

print()
print("-----------------")
print()

for name, details in student_details.items():
    print(name)
    for k, v in details.items():
        print(k, v)

# print(details["anirudh"]["address"])
# print(details["nihar"]["age"])
