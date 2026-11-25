first = input("Enter first string: ")
second = input("Enter second string: ")
normalize = lambda text: sorted(character.lower() for character in text if character.isalnum())
if normalize(first) == normalize(second):
    print("Anagrams")
else:
    print("Not anagrams")
