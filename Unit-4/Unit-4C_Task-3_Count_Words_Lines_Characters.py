with open("sample.txt", "r", encoding="utf-8") as file:
    content = file.read()
print("Number of lines:", len(content.splitlines()))
print("Number of words:", len(content.split()))
print("Number of characters:", len(content))
