import spacy
from catboost import CatBoostClassifier
from loader import load_set
from sklearn.linear_model import LogisticRegression
import pandas as pd

prodigy_model = spacy.load('twitter-spam-model')

def prodigy_predict(value):
  result = prodigy_model(value)
  return result.cats['SPAM']

catboost_model = CatBoostClassifier()
catboost_model.load_model('catboost-model')

training_df = load_set('training')
evaluation_df = load_set('evaluation')

X_train_cat = training_df.drop(columns=['text', 'answer'])
y_train = training_df.answer
X_val_cat = evaluation_df.drop(columns=['text', 'answer'])

cat_predicts = X_train_cat.apply(lambda x: catboost_model.predict_proba([x])[0][1], axis=1)
cat_evaluates = X_val_cat.apply(lambda x: catboost_model.predict_proba([x])[0][1], axis=1)

print(cat_predicts)

X_train_pro = training_df.text
X_val_pro = evaluation_df.text

prodigy_predicts = X_train_pro.apply(lambda x: prodigy_predict(x))
prodigy_evaluates = X_val_pro.apply(lambda x: prodigy_predict(x))

y_val = evaluation_df.answer

print(prodigy_predicts)
 
predictions = pd.DataFrame({ 'prodigy': prodigy_predicts, 'catboost': cat_predicts })
evaluations = pd.DataFrame({ 'prodigy': prodigy_evaluates, 'catboost': cat_evaluates })

logreg = LogisticRegression()

print(logreg.fit(predictions, y_train).score(evaluations, y_val))
