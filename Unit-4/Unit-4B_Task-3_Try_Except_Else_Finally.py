try:
    number = int(input("Enter an integer: "))
except ValueError:
    print("Invalid input. Please enter an integer.")
else:
    print("Square:", number ** 2)
finally:
    print("Program finished")
