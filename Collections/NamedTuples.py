from collections import namedtuple

Student = namedtuple("Student", "name age, marks")
s = Student("Aadi", 19, 95)

print(s.name)
print(s.age)
print(s.marks)