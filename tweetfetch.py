import tweepy
import os
from dotenv import load_dotenv

load_dotenv()

auth = tweepy.AppAuthHandler(
    os.getenv("TWITTER_CONSUMER_KEY"), os.getenv("TWITTER_CONSUMER_SECRET")
)

api = tweepy.API(auth)
for tweet in tweepy.Cursor(api.search, q="tweepy", tweet_mode="extended").items(10):
    print(tweet.full_text)
    print(tweet.retweet_count)
    print(tweet.favorite_count)
    print(tweet.user.followers_count)
