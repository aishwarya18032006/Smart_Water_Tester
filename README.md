# 💧 Smart Water Tester & Purifier 🚰
### 36-Hour Hackathon Project | IoT + AI + Cloud

🏆 **Hackathon Status:** Finalist  
⏱️ **Built in:** 36 Hours    
👥 **Team Members:**  
- Divyasri M  
- Aishwarya R  
---

## 🌍 Problem Statement
Access to clean and safe drinking water is a major challenge.  
Water may look clean but still contain harmful dissolved solids, improper pH levels, or turbidity.

There is a need for a **low-cost, real-time, intelligent water quality monitoring system** that can:
- Detect unsafe water instantly
- Alert users immediately
- Provide historical data and predictions

---

## 💡 Solution Overview
**Smart Water Tester & Purifier** is an IoT + AI based system that:

✔ Measures real-time water parameters  
✔ Uploads data to the cloud  
✔ Uses AI to predict water potability  
✔ Displays live values and graphs on a dashboard  
✔ Alerts users when water is unsafe  

---

## ⚙️ System Architecture

---

## 🧪 Sensors Used
- **pH Sensor** – Measures acidity/alkalinity  
- **TDS Sensor** – Measures total dissolved solids  
- **Turbidity Sensor** – Measures water clarity  
- **DS18B20 Temperature Sensor** – Measures temperature  

---

## 🧠 Working Principle

### 1️⃣ Sensing Layer
Sensors continuously measure:
- pH
- TDS
- Turbidity
- Temperature

### 2️⃣ IoT Layer (ESP32)
- Reads sensor values
- Uploads data to ThingSpeak every 15 seconds
- Activates LED & Buzzer if water is unsafe

### 3️⃣ Cloud Layer (ThingSpeak)
- Stores sensor data
- Generates graphs
- Provides APIs for dashboard & AI model

### 4️⃣ AI Layer
- Machine Learning model trained using Kaggle water potability dataset
- Predicts whether water is **SAFE** or **UNSAFE**

### 5️⃣ Dashboard Layer
- Built using Flask + HTML + CSS + JavaScript
- Shows:
  - Live sensor values
  - SAFE / UNSAFE status
  - Historical graphs

---

## 📊 Results & Observations

| Water Type | TDS (ppm) | Result |
|----------|-----------|--------|
| RO Water | 20 – 50 | ✅ Safe |
| Tap Water | 150 – 250 | ✅ Safe |
| Borewell Water | 300 – 450 | ⚠️ Risk |
| Salt Water | 10000+ | ❌ Unsafe |

✔ AI model successfully classified unsafe samples with high TDS and turbidity.

---

## 🏆 Achievements
- Successfully implemented **real-time IoT monitoring**
- Integrated **cloud + AI + web dashboard**
- Achieved **~78% ML prediction accuracy**
- Built and deployed within **36 hours**
- Low-cost, scalable, and practical solution

---

## 🛠️ Tech Stack
**Hardware**
- ESP32
- pH Sensor
- TDS Sensor
- Turbidity Sensor
- DS18B20
- LED & Buzzer

**Software**
- Python (Flask)
- Machine Learning (Scikit-learn)
- HTML, CSS, JavaScript
- ThingSpeak Cloud
- GitHub & Render (Deployment)

---

## 🚀 Deployment
- Project is deployed using **Render**
- Live dashboard fetches real-time data from ThingSpeak
- Backend API serves AI predictions

---

## 📌 Conclusion
The **Smart Water Tester & Purifier** demonstrates how **IoT, Cloud, and AI** can be combined to solve real-world problems effectively.  
This project can be extended for:
- Smart homes
- Rural water monitoring
- Public water quality systems

---

## 📜 License
This project was developed as part of a **36-hour Hackathon** for educational and research purposes.

---

⭐ If you like this project, give it a star!

