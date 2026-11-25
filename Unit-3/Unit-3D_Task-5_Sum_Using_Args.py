def add_all(*args):
    return sum(args)

values = [float(x) for x in input("Enter numbers separated by spaces: ").split()]
print("Sum =", add_all(*values))
