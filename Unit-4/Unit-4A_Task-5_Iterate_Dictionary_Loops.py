subject_marks = {"Python": 90, "Mathematics": 85, "Physics": 80}
print("Keys:")
for subject in subject_marks.keys():
    print(subject)
print("Values:")
for marks in subject_marks.values():
    print(marks)
print("Items:")
for subject, marks in subject_marks.items():
    print(subject, ":", marks)
