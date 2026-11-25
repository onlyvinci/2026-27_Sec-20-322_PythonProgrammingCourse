a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
c = float(input("Enter third number: "))
if a <= b:
    if a <= c:
        smallest = a
    else:
        smallest = c
else:
    if b <= c:
        smallest = b
    else:
        smallest = c
print("Smallest =", smallest)
