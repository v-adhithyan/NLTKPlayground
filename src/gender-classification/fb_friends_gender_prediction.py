import facebook
import nltk

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
#to hold friends list
friends_list = []
test_set = []
#create a graph api object using the access token obtained from graph api explorer
access_token = get_access_token()
graph = facebook.GraphAPI(access_token=access_token)

#get friend list from facebook
api_response = graph.get_connections(id='me', connection_name='friends')
print api_response
friends = api_response['data'] #get the value of key 'data' which contains json array of friends list
#friends is a json array of dict objects with name and id as keys of each dict object

#iterate each friends and tag them as male or female

train_set = friends[10:] # train first 10 friends in api response
test_set = friends[:10] # remaining will be automatically classified by classifier

genders = []
genders.append((features("ashwini"), "female"))
genders.append((features("krithika"), "female"))
genders.append((features("abinaya"), "female"))
genders.append((features("valli"), "female"))
genders.append((features("sindhuja"), "female"))
genders.append((features("chitra"), "female"))

print "---- Training starts ----"
for friend in train_set:
    name = friend['name']
    gender = raw_input("{} is :".format(name))
    genders.append((features(name), gender))

train_set = genders
classifier = nltk.NaiveBayesClassifier.train(train_set)
print "---- Training ends ----"

print "----- Result ----"
for friend in test_set:
    name = friend['name']
    feature = features(name)
    gender = classifier.classify(feature)
    print "{} is {}".format(name, gender)
