values = input("Enter elements separated by spaces: ").split()
unique = []
for value in values:
    if value not in unique:
        unique.append(value)
print("List without duplicates:", unique)
