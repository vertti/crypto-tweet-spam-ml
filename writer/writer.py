import redis
from json import dumps
from tweet_filter import get_latest_tweets

def construct_json(row):
    return {
      "id": row.id,
      "screen_name": row.screen_name,
      "text": row.full_text,
      "proba": row.logreg,
    }

r = redis.Redis(host="redis", port=6379, db=0)

tweets = get_latest_tweets("$btc", 100)

for row in tweets.itertuples():
  tweet_json = dumps(construct_json(row))
  mapping = { tweet_json: row.timestamp }
  print(mapping)
  r.zadd('btc', mapping)

print(r.zcard("btc"))

