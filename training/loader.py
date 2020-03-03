import pandas as pd
import json
from pandas import json_normalize


def load_set(name):
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
        "cats.SPAM",
    ]
    df = json_normalize(
        pd.Series(open(f"twitter-spam-model/{name}.jsonl").readlines()).apply(
            json.loads
        )
    )
    df = df[df.answer != "ignore"]  # drop lines with unknown result
    return df.drop(columns=non_needed_lines)
