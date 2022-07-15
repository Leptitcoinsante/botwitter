#!/usr/bin/env python
# tweepy-bots/bots/followfollowers.py

from datetime import datetime
import tweepy
import logging
from config import create_api
import time
from models_mongodb import *
from gettweets import GetTweets

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

def follow_followers(api):
    logger.info("Retrieving and following followers")
    for follower in tweepy.Cursor(api.get_followers).items():
        if not follower.following:
            logger.info(f"Following {follower.name}")
            follower.follow()

def post_status(api, lastIdtweeted):
    NewIdTweeted = int(lastIdtweeted) + 1
    Tweet = get_one_tweet(NewIdTweeted)
    # api.update_status(Tweet)
    logger.info(Tweet)
    logger.info("Tweet has been posted!")

    return NewIdTweeted

def main(): 
    api = create_api()
    GetTweets()
    while True:
        now = datetime.now()
        LastTweetPostedInfos = get_LastTweetPostedInfos()
        for document in list(LastTweetPostedInfos):
            lastIdtweeted = document['Idtweeted']
            LastTimestamps = document['LastTimestamps']

        diff = now - datetime.strptime(str(LastTimestamps), '%Y-%m-%d %H:%M:%S.%f')
        if diff.total_seconds() >= 21600.000: # A chaque 6h
            NewTimestamps = now
            follow_followers(api)
            NewIdTweeted = post_status(api, lastIdtweeted)
            filter = {'Idtweeted': lastIdtweeted}
            newvalues = {"$set": {'Idtweeted':NewIdTweeted, 'LastTimestamps':NewTimestamps}}
            update_LastTweetPosted(filter, newvalues)
            
        
        logger.info("Waiting...")
        time.sleep(60)

if __name__ == "__main__":
    main()