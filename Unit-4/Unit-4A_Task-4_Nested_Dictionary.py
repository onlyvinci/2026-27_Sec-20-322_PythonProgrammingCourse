students = {
    1: {"name": "Anu", "marks": 90},
    2: {"name": "Ravi", "marks": 85},
    3: {"name": "Kiran", "marks": 95}
}
for roll_number, details in students.items():
    print("Roll number:", roll_number)
    print("Name:", details["name"])
    print("Marks:", details["marks"])
