from models_mongodb import *

def GetTweets():
    file = open("Tweets.txt","r+", encoding='utf-8')
    #Recuperer le contenu du fichier
    content = []
    chain = ""
    text = str(file.read())
    for i in range(len(text)):
        try:
            int(text[i])
        except ValueError:
            chain = chain + text[i]
        else: 
            if i > 1:   
                content.append(chain)
                chain = ""
                  
    file.close()   
    
    #Ajouter les tweets dans la db
    numbTotaltweet = get_NumbersTweets()
    print(numbTotaltweet)
    for i in range(len(content)):
        numbTotaltweet = numbTotaltweet + 1
        add_tweets(numbTotaltweet, content[i])            
        
    # Effacer le contenu d'un fichier
    f = open("Tweets.txt","w")
    f.close()

