sentence = "python is easy and python is powerful"

word_frequency = {}
for word in sentence.split():
    word_frequency[word] = word_frequency.get(word, 0) + 1

print(word_frequency)
