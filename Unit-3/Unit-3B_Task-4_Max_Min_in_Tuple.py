values = tuple(float(x) for x in input("Enter numbers separated by spaces: ").split())
if values:
    print("Maximum =", max(values))
    print("Minimum =", min(values))
else:
    print("Tuple is empty")
