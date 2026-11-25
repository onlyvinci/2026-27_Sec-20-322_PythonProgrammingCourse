numbers = [10, 20, 30, 40, 50]
try:
    index = int(input("Enter a list index: "))
    print("Value:", numbers[index])
except ValueError:
    print("Please enter a valid integer.")
except IndexError:
    print("Index is outside the list range.")
