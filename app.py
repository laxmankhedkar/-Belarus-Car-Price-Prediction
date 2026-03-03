from flask import Flask, render_template, request
import numpy as np
import pickle
import os

app = Flask(__name__)

# Load model
MODEL_PATH = os.path.join("model", "car_price_model.pkl")
FEATURE_PATH = os.path.join("model", "features.pkl")

with open(MODEL_PATH, "rb") as f:
    model = pickle.load(f)

with open(FEATURE_PATH, "rb") as f:
    features = pickle.load(f)


@app.route('/')
def home():
    return render_template("index.html")


@app.route('/predict', methods=['POST'])
def predict():

    try:
        input_data = []

        for feature in features:
            value = float(request.form.get(feature))
            input_data.append(value)

        final_input = np.array(input_data).reshape(1, -1)

        prediction = model.predict(final_input)

        return render_template(
            "index.html",
            prediction_text=f"Predicted Price: ${round(prediction[0], 2)}"
        )

    except Exception as e:
        return render_template(
            "index.html",
            prediction_text="Error: Please enter valid inputs."
        )


if __name__ == "__main__":
    app.run(debug=True)