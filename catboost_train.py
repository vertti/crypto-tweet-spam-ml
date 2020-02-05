from catboost import CatBoostClassifier
from loader import load_set

training_df = load_set('training').drop(columns=['text'])
evaluation_df = load_set('evaluation').drop(columns=['text'])

X_train = training_df.drop(columns=['answer'])
y_train = training_df.answer

X_val = evaluation_df.drop(columns=['answer'])
y_val = evaluation_df.answer

clf = CatBoostClassifier()
clf.fit(X_train, y_train)
print(f'Accuracy {clf.score(X_val, y_val)}')

clf.save_model('catboost-model')

print(X_train)