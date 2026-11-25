sentence = input("Enter a sentence: ")
frequency = {}
for word in sentence.split():
    word = word.strip(".,!?;:").lower()
    if word:
        frequency[word] = frequency.get(word, 0) + 1
print("Word frequency:", frequency)
