print("Using for loop:")
for i in range(1, 11):
    if i % 2 == 0:
        continue
    print(i)
print("Using while loop:")
i = 0
while i < 10:
    i += 1
    if i % 2 == 0:
        continue
    print(i)
