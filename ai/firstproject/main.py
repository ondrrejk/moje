import data
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

df = pd.DataFrame(data, columns=["height", "weight", "label"])

X = df[["height", "weight"]]
y = df["label"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)

model = LogisticRegression()
model.fit(X_train, y_train)

accuracy = model.score(X_test, y_test)
print("Přesnost:", accuracy)

print(model.predict([[180, 75]]))
