import tweepy
import os
from dotenv import load_dotenv

load_dotenv()


def parse_tweet(tweet):
    print(tweet.created_at)
    print(tweet.full_text)
    print(tweet.retweet_count)  # meta.retweets
    print(tweet.favorite_count)  # meta.favorites
    print(tweet.user.followers_count)  # meta.followers
    print(tweet.user.friends_count)  # meta.friends
    print(len(tweet.entities.get("symbols", {})))  # meta.symbols
    return [
        tweet.full_text,
        tweet.retweet_count,
        tweet.favorite_count,
        tweet.user.followers_count,
        tweet.user.friends_count,
        len(tweet.entities.get("symbols", {})),
    ]


auth = tweepy.AppAuthHandler(
    os.getenv("TWITTER_CONSUMER_KEY"), os.getenv("TWITTER_CONSUMER_SECRET")
)

api = tweepy.API(auth)
for tweet in tweepy.Cursor(api.search, q="$btc", tweet_mode="extended").items(10):
    parse_tweet(tweet)
    if hasattr(tweet, "retweeted_status"):
        print("is retweet")
