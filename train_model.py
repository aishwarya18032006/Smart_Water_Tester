import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import pickle

# Load dataset
data = pd.read_csv("water_quality_data.csv")

# Split into input (X) and output (y)
X = data[['pH', 'TDS', 'Turbidity', 'Temperature']]
y = data['Status'].map({'Safe': 0, 'Unsafe': 1})

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Model
model = RandomForestClassifier(n_estimators=200)

# Train model
model.fit(X_train, y_train)

# Predict
y_pred = model.predict(X_test)

# Accuracy
print("Model Accuracy:", accuracy_score(y_test, y_pred))

# Save trained model
pickle.dump(model, open("water_quality_model.pkl", "wb"))

print("Model saved as water_quality_model.pkl")
