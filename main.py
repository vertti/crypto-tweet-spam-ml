import pandas as pd
import json
from pandas.io.json import json_normalize

def load_set(name):
  non_needed_lines = ['_input_hash', '_task_hash', 'label',
                      'score', 'meta.user_id', 'meta.score', 'spans', 'priority']
  df = json_normalize(pd.Series(
      open(f'twitter-spam-model/{name}.jsonl').readlines()).apply(json.loads))
  return df.drop(columns=non_needed_lines)

training_df = load_set('training')
evaluation_df = load_set('evaluation')
print(evaluation_df)
