text = input("Enter a string: ")
frequency = {}
for character in text:
    frequency[character] = frequency.get(character, 0) + 1
for character, count in frequency.items():
    print(repr(character), ":", count)
