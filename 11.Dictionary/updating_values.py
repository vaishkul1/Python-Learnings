detail = {
    "name": "Anirudh",
    "age": 55,
    "gender": "Male",
}
print(detail)

# Add (if key does not exists)/ update (if key exists)
detail["name"] = "Sanjay"
print(detail)
detail["age"] = 100
print(detail)
detail["address"] = "Surat"
detail["marks"] = [1, 2, 3, 4]
print(detail)


del detail["name"]
print(detail)
