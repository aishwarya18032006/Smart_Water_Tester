import pickle
import requests
import numpy as np

# Your ThingSpeak details
CHANNEL_ID = "3164471"
READ_API_KEY = "X699HIR4ZQX4IRHJ"

# Load trained model and scaler
model = pickle.load(open("models/model.pkl", "rb"))
scaler = pickle.load(open("models/scaler.pkl", "rb"))

# Build the ThingSpeak URL (using Read API Key)
url = f"https://api.thingspeak.com/channels/{CHANNEL_ID}/feeds.json?api_key={READ_API_KEY}&results=1"

# Fetch live data
data = requests.get(url).json()

# Extract the latest field data
feed = data["feeds"][0]

pH = float(feed.get("field1") or 0)
Turbidity = float(feed.get("field2") or 0)
TDS = float(feed.get("field3") or 0)
Temperature = float(feed.get("field4") or 0)

# Map to model features
# Solids ≈ TDS (ppm)
# Conductivity ≈ Temperature (placeholder)
vals = [pH, TDS, Turbidity, Temperature]

print("\nLive Values:", vals)

# Scale input
X_scaled = scaler.transform([vals])

# Predict
prediction = model.predict(X_scaled)[0]

if prediction == 1:
    print("\n✔ SAFE / POTABLE")
else:
    print("\n✖ UNSAFE WATER")
