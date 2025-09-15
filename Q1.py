from collections import Counter

sentence = input("Enter a sentence: ")
words = sentence.lower().split()
word_count = Counter(words)

print("Word Frequencies:")
for word, count in word_count.items():
    print(f"{word}: {count}")
