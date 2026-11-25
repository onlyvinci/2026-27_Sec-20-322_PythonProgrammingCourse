with open("sample.txt", "r", encoding="utf-8") as source_file:
    content = source_file.read()
with open("copy.txt", "w", encoding="utf-8") as destination_file:
    destination_file.write(content)
print("File copied successfully.")
