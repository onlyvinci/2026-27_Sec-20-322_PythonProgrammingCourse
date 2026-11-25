n = int(input("Enter N: "))
print("Using for loop:")
for number in range(1, n + 1):
    print(number, end=" ")
print("\nUsing while loop:")
number = 1
while number <= n:
    print(number, end=" ")
    number += 1
print()
