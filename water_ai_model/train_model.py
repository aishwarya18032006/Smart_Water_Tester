import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
import pickle
import os

# Dataset path
DATA_PATH = "data/water_potability.csv"

print("Loading dataset...")
df = pd.read_csv(DATA_PATH)
print("Dataset loaded successfully!")

print("\nColumns in dataset:")
print(df.columns.tolist())

# Fill missing values using median
df.fillna(df.median(), inplace=True)

# These columns exist in the water_potability.csv dataset
# We will use these 4 as features:
features = ["ph", "Solids", "Turbidity", "Conductivity"]

print("\nUsing features:", features)

X = df[features]
y = df["Potability"]   # 1 = drinkable, 0 = not drinkable

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Scale the data
scaler = StandardScaler()
X_train_s = scaler.fit_transform(X_train)
X_test_s = scaler.transform(X_test)

# Train Random Forest model
model = RandomForestClassifier(n_estimators=200, random_state=42)
model.fit(X_train_s, y_train)

# Predictions
y_pred = model.predict(X_test_s)

print("\nModel Accuracy:", accuracy_score(y_test, y_pred))
print("\nClassification Report:")
print(classification_report(y_test, y_pred))

# Save model and scaler
os.makedirs("models", exist_ok=True)
pickle.dump(model, open("models/model.pkl", "wb"))
pickle.dump(scaler, open("models/scaler.pkl", "wb"))

print("\nModel trained successfully!")
print("Saved as models/model.pkl and models/scaler.pkl")
