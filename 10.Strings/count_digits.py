a = "my age is 28 and uhiehifufjekw.#$%^&77"
"""  
count = 0
for ch in a:
    if ch=="0" or ch=="1" etc:
        count+=1
"""
count = 0
for ch in a:
    if ord(ch) >= 48 or ord(ch) <= 57:
        count += 1
print(count)
