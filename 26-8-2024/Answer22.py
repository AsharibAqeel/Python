text = input("Enter the text: ").split()

word_count = {}

for word in text:
    word_count[word] = word_count.get(word, 0) + 1

for word in sorted(word_count.keys()):
    print(f"{word}:{word_count[word]}")
