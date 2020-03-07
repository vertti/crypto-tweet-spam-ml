from catboost import CatBoostClassifier
from loader import load_set
from sklearn.model_selection import train_test_split

train = load_set().drop(columns=["text"])

X = train.drop(columns=["answer"])
y = train.answer

X_train, X_val, y_train, y_val = train_test_split(X, y)

clf = CatBoostClassifier()
clf.fit(X_train, y_train)
print(f"Accuracy {clf.score(X_val, y_val)}")

clf.save_model("catboost-model")

print(X_train)
