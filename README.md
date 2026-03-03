# 🚗 Belarus Car Price Prediction App

A Machine Learning web application that predicts car prices based on key vehicle features.  
Built using **Scikit-learn** and deployed using **Flask**.

---

## 📌 Project Overview

This project predicts the resale price of cars listed in Belarus using:

- Year of manufacture
- Engine volume (cm³)
- Fuel type
- Transmission type
- Make segment
- Drive unit

The model is trained using a Random Forest Regressor and deployed as a Flask web application.

---

## 🧠 Machine Learning Pipeline

### 1️⃣ Data Preprocessing
- Handled missing values
- Encoded categorical features
- Feature selection using feature importance

### 2️⃣ Model Training
- RandomForestRegressor
- Train/Test split validation
- Performance evaluation using R² score

### 3️⃣ Model Serialization
- Model saved using `pickle`
- Feature list stored for consistent prediction input

### 4️⃣ Deployment
- Flask backend
- HTML frontend
- Structured project architecture

---
```
Belarus-Car-Price-Prediction/
│
├── app.py                  # Flask application
├── requirements.txt        # Project dependencies
│
├── model/                  # Saved ML artifacts
│   ├── car_price_model.pkl
│   └── features.pkl
│
├── templates/              # HTML templates
│   └── index.html
│
└── static/                 # CSS / static files (optional)


```
---
## 💻 Tech Stack

- Python 3.13
- Pandas
- NumPy
- Scikit-learn
- Flask
- Pickle
- HTML

---

## 🚀 How to Run the Project

### 1️⃣ Clone the repository

git clone https://github.com/YOUR_USERNAME/belarus-car-price-prediction.git  
cd belarus-car-price-prediction  

### 2️⃣ Install dependencies

python -m pip install -r requirements.txt  

### 3️⃣ Run the Flask App

python app.py  

### 4️⃣ Open in Browser

http://127.0.0.1:5000/

---

## 📊 Sample Prediction

Example Input:

- Year: 2018  
- Engine Volume: 1800 cm³  
- Fuel Type: Diesel  
- Transmission: Automatic  
- Make Segment: Mid  
- Drive Unit: AWD  

Output:

Predicted Price: $29,659.91

---

## 🎯 Key Features

✔ End-to-end ML pipeline  
✔ Feature selection using importance ranking  
✔ Model deployment with Flask  
✔ Clean structured folder architecture  
✔ Production-ready setup  

---

## 📈 Future Improvements

- Add Bootstrap styling
- Replace numeric encodings with dropdown labels
- Add REST API endpoint
- Deploy on Render / Railway
- Docker containerization

---

## 👨‍💻 Author

**Laxman Bhimrao Khedkar**  
Data Analyst | Machine Learning Enthusiast  

🔗 LinkedIn: https://www.linkedin.com/in/laxman-khedkar  
🔗 Portfolio: https://beacons.ai/laxmankhedkar  
🔗 GitHub: https://github.com/laxmankhedkar  

---

## ⭐ If You Like This Project

Give it a ⭐ on GitHub and feel free to contribute!
