import nltk
sentence = """the book is with the books having fun looking tired"""

stemmer = nltk.SnowballStemmer("english")
tokens = nltk.word_tokenize(sentence)
for token in tokens:
    print (stemmer.stem(token))
    