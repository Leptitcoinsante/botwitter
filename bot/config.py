import tweepy
import logging
import os

logger = logging.getLogger()

def create_api():
    consumer_key = os.environ.get(consumer_key)
    consumer_secret = os.environ.get(consumer_secret)
    access_token = os.environ.get(access_token)
    access_token_secret = os.environ.get(access_token_secret)

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth, wait_on_rate_limit=True)
    try:
        api.verify_credentials()
    except Exception as e:
        logger.error("Error creating API", exc_info=True)
        raise e
    logger.info("API created")
    return api