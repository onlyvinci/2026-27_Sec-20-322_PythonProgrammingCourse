rows = int(input("Enter number of rows in upper half: "))
for i in range(1, rows + 1):
    if i == 1:
        print(" " * (rows - i) + "*")
    else:
        print(" " * (rows - i) + "*" + " " * (2 * i - 3) + "*")
for i in range(rows - 1, 0, -1):
    if i == 1:
        print(" " * (rows - i) + "*")
    else:
        print(" " * (rows - i) + "*" + " " * (2 * i - 3) + "*")
