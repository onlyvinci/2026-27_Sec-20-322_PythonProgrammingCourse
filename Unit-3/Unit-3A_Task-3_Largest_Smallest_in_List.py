numbers = [float(x) for x in input("Enter numbers separated by spaces: ").split()]
if numbers:
    print("Largest =", max(numbers))
    print("Smallest =", min(numbers))
else:
    print("List is empty")
