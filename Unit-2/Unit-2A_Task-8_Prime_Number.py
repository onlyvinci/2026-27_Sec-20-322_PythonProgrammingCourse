number = int(input("Enter a number between 1 and 100: "))
is_prime = number >= 2
for divisor in range(2, int(number ** 0.5) + 1):
    if number % divisor == 0:
        is_prime = False
        break
print("Prime number" if is_prime else "Not a prime number")
