from flask import Flask, request, render_template
import numpy as np
import pickle
import sklearn
import pandas as pd

# importing model
model = pickle.load(open('model.pkl', 'rb'))

# creating flask app
app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")


@app.route("/predict", methods=['POST'])
def predict():
    # Collecting input features from the form
    float_features = [float(x) for x in request.form.values()]
    # print("Received input features:", float_features)  # Debugging

    # Defining the feature names as used during the model training
    feature_names = ['Sepal_Length', 'Sepal_Width', 'Petal_Length', 'Petal_Width']

    # Creating a DataFrame with the feature names
    features = pd.DataFrame([float_features], columns=feature_names)
    # print("DataFrame created:", features)  # Debugging

    # Making predictions
    prediction = model.predict(features)
    # print("Prediction:", prediction)  # Debugging

    # Rendering the template with the prediction result
    return render_template("index.html", prediction_text="The Species of the Iris Flower is {}".format(prediction[0]))


# Main function to run the Flask app
if __name__ == "__main__":
    app.run(debug=True)
