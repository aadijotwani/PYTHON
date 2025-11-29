d = {"name": "Aadi", "age": 19}

d["age"] = 20
print(d.keys())
print(d.values())
print(d.items())
d.pop("age")
print(d)
d.update({"city":"bhopal" })
print(d)

for k, v in d.items():
    print(k, v)