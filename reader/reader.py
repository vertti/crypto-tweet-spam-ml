import redis
from json import loads

r = redis.Redis(host="redis", port=6379, db=0, decode_responses=True)


def get_tweets(coin: str):
    response = r.zrevrange(f"{coin}", 0, 10)
    print(f'got response {response}', flush=True)
    return [loads(tweet) for tweet in response]
