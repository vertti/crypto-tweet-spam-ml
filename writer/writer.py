import redis
from json import dumps
from pandas import DataFrame

def construct_json(row):
    return {
      "id": row.id,
      "screen_name": row.screen_name,
      "text": row.full_text,
      "proba": row.logreg,
    }

r = redis.Redis(host="redis", port=6379, db=0)

def store_tweets(coin: str, tweets: DataFrame):
    for row in tweets.itertuples():
      tweet_json = dumps(construct_json(row))
      mapping = { tweet_json: row.timestamp }
      print(mapping)
      r.zadd('btc', mapping)

    print(r.zcard("btc"))

