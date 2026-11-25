text = input("Enter a string: ")
vowels = consonants = digits = spaces = 0
for character in text:
    if character.lower() in "aeiou":
        vowels += 1
    elif character.isalpha():
        consonants += 1
    elif character.isdigit():
        digits += 1
    elif character.isspace():
        spaces += 1
print("Vowels:", vowels)
print("Consonants:", consonants)
print("Digits:", digits)
print("Spaces:", spaces)
