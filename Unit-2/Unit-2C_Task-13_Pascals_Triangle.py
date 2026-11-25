rows = int(input("Enter number of rows: "))
for i in range(rows):
    print(" " * (rows - i), end="")
    value = 1
    for j in range(i + 1):
        print(value, end=" ")
        value = value * (i - j) // (j + 1)
    print()
