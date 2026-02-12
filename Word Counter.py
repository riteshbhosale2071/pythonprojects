# Word Counter - A simple program to count characters, words, and sentences in a given text.
text = input("Enter a sentence or paragraph: ")

# characters
char_count = len(text)

# words
words = text.split()
word_count = len(words)

# sentences
sentence_count = text.count('.') + text.count('!') + text.count('?')

print("\nResults:")
print("Characters:", char_count)
print("Words:", word_count)
print("Sentences:", sentence_count)