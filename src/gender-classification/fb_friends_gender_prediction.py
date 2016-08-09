import facebook
import nltk
import requests
from nltk.corpus import names
import random

def get_access_token():
    """
    create a text file with name access_token.txt in the same directory of this src file
    and insert your access token obtained from graph api explorer.
    """
    token = ""
    with open("access_token.txt", "r") as f:
        token = f.read()
    return token

def features(name):
    return {'suffix1' : name[-1:],
            'suffix2' : name[-2:],
            'suffix3' : name[-3:]}


#create a graph api object using the access token obtained from graph api explorer
access_token = get_access_token()
graph = facebook.GraphAPI(access_token=access_token)

#get friend list from facebook
api_response = graph.get_connections(id='me', connection_name='friends')
friends = api_response['data'] #get the value of key 'data' which contains json array of friends list
#friends is a json array of dict objects with name and id as keys of each dict object

#train with nltk corpus names
names = ([(name, 'male') for name in names.words('male.txt')] +
         [(name, 'female') for name in names.words('female.txt')])
random.shuffle(names)
featuresets = [(features(n), g) for (n, g) in names]

classifier = nltk.NaiveBayesClassifier.train(featuresets)

#classify facebook friends gender
for friend in friends:
    name = friend['name']
    gender = classifier.classify(features(name))
    print "{} is {}".format(name, gender)
