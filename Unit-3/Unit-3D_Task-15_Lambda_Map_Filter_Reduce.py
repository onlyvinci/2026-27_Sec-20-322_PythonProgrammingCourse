from functools import reduce

numbers = [int(x) for x in input("Enter numbers separated by spaces: ").split()]
squares = list(map(lambda x: x * x, numbers))
evens = list(filter(lambda x: x % 2 == 0, numbers))
total = reduce(lambda a, b: a + b, numbers, 0)
print("Squares:", squares)
print("Even numbers:", evens)
print("Sum:", total)
