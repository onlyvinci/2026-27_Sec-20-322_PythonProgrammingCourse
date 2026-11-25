student = {"name": "Anu", "age": 18, "course": "CSE"}
print("Keys:", student.keys())
print("Values:", student.values())
print("Items:", student.items())
print("Name:", student.get("name"))
student.update({"age": 19})
print("After update:", student)
student.pop("course")
print("After pop:", student)
