import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

# Load data
data = pd.read_csv("data/patients.csv")

# Convert condition text into numbers
data["condition_code"] = data["condition"].astype("category").cat.codes

# Features (X) and target (y)
X = data[["age", "condition_code"]]
y = (data["risk_score"] > 0.7).astype(int)  # High risk = 1, Low risk = 0

# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Train model
model = LogisticRegression()
model.fit(X_train, y_train)

# Accuracy
accuracy = model.score(X_test, y_test)
print("Model accuracy:", accuracy)
