from nltk.corpus import names
import nltk
import random

def gender_features(word):
    return {'suffix1' : word[-1:],
            'suffix2' : word[-2:],
            'suffix3' : word[-3:]}

names = ([(name, 'male') for name in names.words('male.txt')] +
         [(name, 'female') for name in names.words('female.txt')])
random.shuffle(names)

featuresets = [(gender_features(n), g) for (n, g) in names]
train_set, devtest_set, test_set = featuresets[1500:], featuresets[500:1500], featuresets[:500]
classifier = nltk.NaiveBayesClassifier.train(train_set)
#print nltk.classify.accuracy(classifier, test_set)


while True:
    name = raw_input("Enter a name:")
    feature = gender_features(name)
    gender = classifier.classify(feature)
    print "{} is a {}".format(name, gender)
