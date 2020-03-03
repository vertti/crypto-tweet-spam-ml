import pandas as pd
from datetime import datetime
import tweepy
import os
from dotenv import load_dotenv

load_dotenv()


def parse_tweet(tweet):
    parsed = [
        int(datetime.timestamp(tweet.created_at)),
        tweet.id,
        tweet.user.screen_name,
        tweet.full_text,
        tweet.retweet_count,
        tweet.favorite_count,
        tweet.user.followers_count,
        tweet.user.friends_count,
        len(tweet.entities.get("symbols", {})),
    ]
    return parsed


auth = tweepy.AppAuthHandler(
    os.getenv("TWITTER_CONSUMER_KEY"), os.getenv("TWITTER_CONSUMER_SECRET")
)

api = tweepy.API(auth)

def fetch_tweet_df(search_term: str, limit: int) -> pd.DataFrame:
    data = [
        parse_tweet(tweet)
        for tweet in tweepy.Cursor(api.search, q=search_term, result_type="recent", tweet_mode="extended", include_entities=True).items(limit)
        if not hasattr(tweet, "retweeted_status")
    ]

    tweet_df = pd.DataFrame(
        data,
        columns=[
            "timestamp",
            "id",
            "screen_name",
            "full_text",
            "meta.retweets",
            "meta.favorites",
            "meta.followers",
            "meta.friends",
            "meta.symbols",
        ],
    )
    print(tweet_df)
    return tweet_df
