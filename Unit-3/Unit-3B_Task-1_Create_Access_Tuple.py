values = tuple(input("Enter tuple elements separated by spaces: ").split())
print("Tuple:", values)
if values:
    print("First element:", values[0])
    print("Last element:", values[-1])
    for value in values:
        print(value)
