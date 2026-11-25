n = int(input("How many numbers? "))
total = 0
for i in range(n):
    value = float(input("Enter number: "))
    total += value
if n > 0:
    print("Sum =", total)
    print("Average =", total / n)
else:
    print("Enter at least one number")
