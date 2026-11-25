number = int(input("Enter a three-digit number: "))
original = number
total = 0
while number > 0:
    digit = number % 10
    total += digit ** 3
    number //= 10
if original == total:
    print("Armstrong number")
else:
    print("Not an Armstrong number")
