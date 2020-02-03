import spacy
from catboost import CatBoostClassifier

prodigy_model = spacy.load('twitter-spam-model')

catboost_model = CatBoostClassifier()
catboost_model.load_model('catboost-model')
