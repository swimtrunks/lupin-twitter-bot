import os as _os
import dotenv as _dotenv
import time as _time
import tweepy as _tweepy

import services as _services

_dotenv.load_dotenv()

API_KEY = _os.environ["TWITTER_API_KEY"]
SECRET_KEY = _os.environ["TWITTER_API_SECRET"]
ACCESS_TOKEN = _os.environ["TWITTER_ACCESS_TOKEN"]
ACCESS_TOKEN_SECRET = _os.environ["TWITTER_ACCESS_TOKEN_SECRET"]


def _get_twitter_api():
    auth = _tweepy.OAuthHandler(API_KEY, SECRET_KEY)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
    twitter_api = _tweepy.API(
        auth, wait_on_rate_limit=True, 
        #wait_on_rate_limit_notify=True --todo: bug fix
    )
    
    return twitter_api

def _write_tweet():
    tweet= _services.get_tweet()
    twitter_api = _get_twitter_api()
    twitter_api.update_status(tweet)

def run():
    while True:
        _write_tweet()
        _time.sleep(3600) #1hour
        # _time.sleep(10)
        #is there a way to post at a specific time in addition to intervals?

if __name__ == "__main__":
    run()
