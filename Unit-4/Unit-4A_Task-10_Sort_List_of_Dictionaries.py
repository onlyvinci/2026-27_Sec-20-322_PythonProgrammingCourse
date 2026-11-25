students = [
    {"name": "Anu", "marks": 85},
    {"name": "Ravi", "marks": 95},
    {"name": "Kiran", "marks": 75}
]
ascending = sorted(students, key=lambda student: student["marks"])
descending = sorted(students, key=lambda student: student["marks"], reverse=True)
print("Ascending order:")
for student in ascending:
    print(student)
print("Descending order:")
for student in descending:
    print(student)
