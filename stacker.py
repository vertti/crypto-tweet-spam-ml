import spacy
from catboost import CatBoostClassifier
from sklearn.ensemble import StackingClassifier
from loader import load_set

prodigy_model = spacy.load('twitter-spam-model')

catboost_model = CatBoostClassifier()
catboost_model.load_model('catboost-model')

clf = StackingClassifier(
    estimators=[('prodigy', prodigy_model), ('catboost', catboost_model)],
)

training_df = load_set('training')
evaluation_df = load_set('evaluation')

X_train = training_df.drop(columns=['answer'])
y_train = training_df.answer

X_val = evaluation_df.drop(columns=['answer'])
y_val = evaluation_df.answer

print(clf.fit(X_train, y_train).score(X_val, y_val))