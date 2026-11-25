with open("sample.txt", "r", encoding="utf-8") as file:
    content = file.read()
old_word = input("Enter word to replace: ")
new_word = input("Enter replacement word: ")
content = content.replace(old_word, new_word)
with open("sample.txt", "w", encoding="utf-8") as file:
    file.write(content)
print("Word replaced successfully.")
