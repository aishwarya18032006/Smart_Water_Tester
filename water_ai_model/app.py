from flask import Flask, jsonify, render_template
from flask_cors import CORS
import requests
import pickle
import numpy as np

app = Flask(__name__)
CORS(app)

# ThingSpeak Info
CHANNEL_ID = "3164471"
READ_API_KEY = "X699HIR4ZQX4IRHJ"
TS_URL = f"https://api.thingspeak.com/channels/{CHANNEL_ID}/feeds.json?api_key={READ_API_KEY}&results=1"

# Load AI model & scaler
model = pickle.load(open("models/model.pkl", "rb"))
scaler = pickle.load(open("models/scaler.pkl", "rb"))

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/api/predict")
def predict():
    try:
        r = requests.get(TS_URL)
        data = r.json()

        feed = data["feeds"][0]

        # SAFE PARSING (avoid None → crash)
        ph = float(feed.get("field1") or 0)
        turb = float(feed.get("field2") or 0)
        tds = float(feed.get("field3") or 0)
        temp = float(feed.get("field4") or 0)

        # AI Prediction
        features = np.array([[ph, tds, turb, temp]])
        scaled = scaler.transform(features)
        pred = model.predict(scaled)[0]

        status = "SAFE" if pred == 1 else "UNSAFE"

        return jsonify({
            "success": True,
            "values": {
                "pH": ph,
                "TDS": tds,
                "Turbidity": turb,
                "Temperature": temp
            },
            "prediction": status
        })

    except Exception as e:
        return jsonify({"success": False, "error": str(e)})

if __name__ == "__main__":
    app.run(debug=True)
