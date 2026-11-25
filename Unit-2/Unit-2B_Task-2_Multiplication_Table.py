number = int(input("Enter a number: "))
print("Using for loop:")
for i in range(1, 11):
    print(number, "x", i, "=", number * i)
print("Using while loop:")
i = 1
while i <= 10:
    print(number, "x", i, "=", number * i)
    i += 1
