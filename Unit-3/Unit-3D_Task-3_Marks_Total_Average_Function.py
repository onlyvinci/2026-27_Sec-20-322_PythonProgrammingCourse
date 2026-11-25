def calculate_marks(mark1, mark2, mark3):
    total = mark1 + mark2 + mark3
    average = total / 3
    return total, average

a = float(input("Enter marks in subject 1: "))
b = float(input("Enter marks in subject 2: "))
c = float(input("Enter marks in subject 3: "))
total, average = calculate_marks(a, b, c)
print("Total =", total)
print("Average =", average)
