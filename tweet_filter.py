import pandas as pd
import pickle
import spacy
from catboost import CatBoostClassifier
from tweetfetch import fetch_tweet_df

prodigy_model = spacy.load("twitter-spam-model")


def get_proba(tuplelist):
    return list(map(lambda tuple: tuple[0], tuplelist))


def prodigy_predict(value):
    result = prodigy_model(value)
    return result.cats["SPAM"]


catboost_model = CatBoostClassifier()
catboost_model.load_model("catboost-model")

logreg_model = pickle.load(open("logreg_model.sav", "rb"))


def get_latest_tweets(search_term: str, limit: int) -> pd.DataFrame:
    tweets = fetch_tweet_df(search_term, limit)

    cat_predictions = get_proba(
        catboost_model.predict_proba(
            tweets.drop(columns=["full_text", "id", "screen_name"])
        )
    )

    tweets["catboost"] = cat_predictions
    tweets["prodigy"] = tweets["full_text"].apply(prodigy_predict)

    logreg_data = tweets[["prodigy", "catboost"]]

    logreg_proba = get_proba(logreg_model.predict_proba(logreg_data))
    tweets["logreg"] = logreg_proba

    return tweets
