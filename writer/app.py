from tweet_filter import get_latest_tweets
from coinmarket import get_top_coins
from writer import store_tweets
from time import sleep

print("Fetching top coins")

top_coins = get_top_coins(50)

print("Current top coins", top_coins)

while True:
    for coin in top_coins:
        print(f"Fetching tweets for ${coin}")
        tweets = get_latest_tweets(f"${coin}", 100)
        if len(tweets.index) > 0:
            print(f"Storing tweets for ${coin}")
            store_tweets(coin, tweets)
        else:
            print("No tweets found")
        sleep(10)

    print("Finished writing 100 most recent tweets for each 50 top coins")
    print("Sleeping 2 minutes")
    sleep(120)
    print("Woke up")
