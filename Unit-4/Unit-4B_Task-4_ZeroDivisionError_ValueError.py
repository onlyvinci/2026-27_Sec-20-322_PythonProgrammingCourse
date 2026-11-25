try:
    numerator = float(input("Enter numerator: "))
    denominator = float(input("Enter denominator: "))
    print("Result:", numerator / denominator)
except ZeroDivisionError:
    print("Cannot divide by zero.")
except ValueError:
    print("Please enter valid numbers.")
