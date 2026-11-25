text = input("Enter a line of text: ")
with open("output.txt", "w", encoding="utf-8") as file:
    file.write(text + "\n")
print("Text written successfully.")
