import pandas as pd
import json
from pandas import json_normalize
from os import path

def load_set():
    non_needed_lines = [
        "_session_id",
        "_view_id",
        "_input_hash",
        "_task_hash",
        "label",
        "score",
        "meta.user_id",
        "meta.score",
        "spans",
        "priority",
        "meta.pattern",
    ]
    df = json_normalize(
        pd.Series(open(path.join("..", "models", "twitter-spam-model", "twitter_spam.jsonl")).readlines()).apply(
            json.loads
        )
    )
    df = df[df.answer != "ignore"]  # drop lines with unknown result
    return df.drop(columns=non_needed_lines)
