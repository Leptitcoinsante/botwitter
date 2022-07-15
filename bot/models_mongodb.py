from pymongo import MongoClient

# se connecter à MongoDB, modifier le << MONGODB URL >> pour refléter votre propre chaîne de connexion
client = MongoClient("mongodb+srv://root:root@bottwi.mc8jseb.mongodb.net/?retryWrites=true&w=majority")
# Client.databasename
db = client.TweetsContent

# Add an user to database
def add_tweets(Idtweet, Content):
    #Etape 2: Créer des exemples de données
    Tweet = {
            'Idtweet': Idtweet,
            'Content': Content
        }
    #Etape 3: Insérer l'objet métier directement dans MongoDB via isnert_one
    result = db.tweets.insert_one(Tweet)
    #Etape 4: Imprimer sur la console l'ObjectID du nouveau document
    return f'Enregistré dans en tant que : ', {result.inserted_id}

def get_NumbersTweets():
    result = db.tweets.count()
    return result

def get_one_tweet(Idtweet):
    tweet = db.tweets.find_one({'Idtweet':Idtweet})
    return tweet

def delete_one_tweet(Idtweet):
    result = db.tweets.delete_one({'Idtweet':Idtweet})
    return result



def add_LastTweetPosted(Idtweeted, LastTimestamps):
    #Etape 2: Créer des exemples de données
    LastTweetPosted = {
                       'Idtweeted': Idtweeted,
                       'LastTimestamps': LastTimestamps
                    }
    #Etape 3: Insérer l'objet métier directement dans MongoDB via isnert_one
    result = db.LastTweetPosted.insert_one(LastTweetPosted)
    #Etape 4: Imprimer sur la console l'ObjectID du nouveau document
    return f'Enregistré dans en tant que : ', {result.inserted_id}    

def get_LastTweetPostedInfos():
    result = db.LastTweetPosted.find()
    return result

def update_LastTweetPosted(filter, newvalues):
    result = db.LastTweetPosted.update_one(filter, newvalues)
    return result
     
