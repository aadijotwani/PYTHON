from functools import reduce

nums = [1,2]
result = reduce(lambda a, b: a+b, nums)

print(result)


try:
    age = int(input("Enter age: "))
    if age < 0:
        raise ValueError("Age cannot be negative")
except ValueError as e:
    print("Error:", e)


D = {"Name": "Aadi", "Age": 12}
print(D.values())