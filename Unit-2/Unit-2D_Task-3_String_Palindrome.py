text = input("Enter a string: ")
cleaned = "".join(character.lower() for character in text if character.isalnum())
if cleaned == cleaned[::-1]:
    print("Palindrome")
else:
    print("Not a palindrome")
