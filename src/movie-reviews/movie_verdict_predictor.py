from nltk.corpus import movie_reviews
import nltk
import random



documents = [(list(movie_reviews.words(fileid)), category)
             for category in movie_reviews.categories()
             for fileid in movie_reviews.fileids(category)]
random.shuffle(documents)

all_words = nltk.FreqDist(w.lower() for w in movie_reviews.words())
word_features = all_words.keys()[:2000]

def document_features(document):
    document_words = set(document)
    features = {}
    for word in word_features:
        features['contains(%s)' % word] = word in document_words
    return features

def find_review_sentiment(filename):
    with open(filename, "r") as f:
        review = f.read()
        features = document_features(review.split(" "))
        print classifier.classify(features)

featuresets = [(document_features(d), c) for (d, c) in documents]
train_set = featuresets
classifier = nltk.NaiveBayesClassifier.train(train_set)

find_review_sentiment("thuppakki.txt")
find_review_sentiment("kabali.txt")
