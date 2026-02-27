import data
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
# from sklearn.preprocessing import StandardScaler
# import matplotlib.pyplot as plt

df = pd.DataFrame(data, columns=["height", "weight", "label"])
X = df[["height", "weight"]]
y = df["label"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42
)

model = KNeighborsClassifier(n_neighbors=3)
model.fit(X_train, y_train)

accuracy = model.score(X_test, y_test)
print("Přesnost:", accuracy)

print(model.predict([[182, 82]]))


# --- SCALER ---
# scaler = StandardScaler()
# X_train_scaled = scaler.fit_transform(X_train)
# X_test_scaled = scaler.transform(X_test)

# model = KNeighborsClassifier(n_neighbors=3)
# model.fit(X_train_scaled, y_train)

# print(model.score(X_test_scaled, y_test))


# --- MATPLOTLIB ---
# plt.scatter(df["height"], df["weight"], c=df["label"])
# plt.xlabel("Height")
# plt.ylabel("Weight")
# plt.show()
