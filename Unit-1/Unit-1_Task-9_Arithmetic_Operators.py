a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
print("Addition =", a + b)
print("Subtraction =", a - b)
print("Multiplication =", a * b)
if b != 0:
    print("Division =", a / b)
    print("Floor division =", a // b)
    print("Modulus =", a % b)
else:
    print("Division, floor division and modulus are undefined for zero divisor")
print("Power =", a ** b)
