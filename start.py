import nltk



fileLines = open('abc.txt', 'r').readlines()
tokens = []
i = 0

while i < len(fileLines):
    tokens.append(nltk.word_tokenize(fileLines[i]))
    i += 1

print(tokens)