n = int(input("How many numbers? "))
if n <= 0:
    print("Enter at least one number")
else:
    largest = float(input("Enter number: "))
    for i in range(n - 1):
        value = float(input("Enter number: "))
        if value > largest:
            largest = value
    print("Largest =", largest)
