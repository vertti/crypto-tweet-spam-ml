import pickle
import spacy
from catboost import CatBoostClassifier
from loader import load_set
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
import pandas as pd
from os import path

prodigy_model = spacy.load(path.join("..", "models", "twitter-spam-model"))


def prodigy_predict(value):
    result = prodigy_model(value)
    return result.cats["SPAM"]


catboost_model = CatBoostClassifier()
catboost_model.load_model(path.join("..", "models", "catboost-model"))

train = load_set()

print(train.head())

X = train.drop(columns=["answer"])
y = train.answer

X_train, X_val, y_train, y_val = train_test_split(X, y)

X_train_cat = X_train.drop(columns=["text"])
X_val_cat = X_val.drop(columns=["text"])
X_train_pro = X_train.text
X_val_pro = X_val.text

cat_predicts = X_train_cat.apply(
    lambda x: catboost_model.predict_proba([x])[0][0], axis=1
)
cat_evaluates = X_val_cat.apply(
    lambda x: catboost_model.predict_proba([x])[0][0], axis=1
)

print(cat_predicts)

prodigy_predicts = X_train_pro.apply(lambda x: prodigy_predict(x))
prodigy_evaluates = X_val_pro.apply(lambda x: prodigy_predict(x))

print(prodigy_predicts)

predictions = pd.DataFrame({"prodigy": prodigy_predicts, "catboost": cat_predicts})
evaluations = pd.DataFrame({"prodigy": prodigy_evaluates, "catboost": cat_evaluates})

print(predictions)

logreg = LogisticRegression()

print(logreg.fit(predictions, y_train).score(evaluations, y_val))

filename = "logreg_model.sav"
pickle.dump(logreg, open(filename, "wb"))
