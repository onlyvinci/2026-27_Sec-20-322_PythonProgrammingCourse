def factorial(n):
    if n < 0:
        raise ValueError("Enter a non-negative integer")
    if n <= 1:
        return 1
    return n * factorial(n - 1)

number = int(input("Enter a number: "))
print("Factorial =", factorial(number))
