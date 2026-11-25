numbers = [int(x) for x in input("Enter numbers separated by spaces: ").split()]
value = int(input("Enter value to insert: "))
numbers.insert(0, value)
numbers.append(value)
if numbers:
    numbers.remove(value)
numbers.sort()
print("Sorted list:", numbers)
numbers.reverse()
print("Reversed list:", numbers)
