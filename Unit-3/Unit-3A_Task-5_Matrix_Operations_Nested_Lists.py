rows = int(input("Enter number of rows: "))
columns = int(input("Enter number of columns: "))
matrix = []
for i in range(rows):
    row = [int(x) for x in input("Enter row elements: ").split()]
    while len(row) != columns:
        print("Enter exactly", columns, "values")
        row = [int(x) for x in input("Enter row elements: ").split()]
    matrix.append(row)
print("Matrix:")
for row in matrix:
    print(*row)
print("Transpose:")
for j in range(columns):
    print(*(matrix[i][j] for i in range(rows)))
