import pandas as pd
import json
from pandas.io.json import json_normalize
from catboost import CatBoostClassifier

def load_set(name):
  non_needed_lines = ['text', '_input_hash', '_task_hash', 'label',
                      'score', 'meta.user_id', 'meta.score', 'spans', 'priority']
  df = json_normalize(pd.Series(
      open(f'twitter-spam-model/{name}.jsonl').readlines()).apply(json.loads))
  df = df[df.answer != 'ignore'] # drop lines with unknown result
  return df.drop(columns=non_needed_lines)

training_df = load_set('training')
evaluation_df = load_set('evaluation')

X_train = training_df.drop(columns=['answer'])
y_train = training_df.answer

X_val = evaluation_df.drop(columns=['answer'])
y_val = evaluation_df.answer

clf = CatBoostClassifier()
clf.fit(X_train, y_train)
print(f'Accuracy {clf.score(X_val, y_val)}')

clf.save_model('catboost-model')