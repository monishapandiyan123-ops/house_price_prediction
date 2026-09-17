from flask import Flask, request, render_template
import joblib
import pandas as pd

app = Flask(__name__)

# Load the trained ML model
model = joblib.load("House_price_prediction_model.joblib")


# Home page
@app.route("/")
def home():
    return render_template("index.html")


# Prediction endpoint
@app.route("/predict", methods=["POST"])
def predict():

    # Get input from HTML form
    city = str(request.form["city"])
    yr_built_bin = str(request.form["yr_built_bin"])
    #age = int(request.form["age"])
    sqft_basement = int(request.form["sqft_basement"])
    sqft_above = int(request.form["sqft_above"])
    total_rooms = int(request.form["total_rooms"])
    floors = int(request.form["floors"])
    view = int(request.form["view"])
    waterfront = int(request.form["waterfront"])
    condition = int(request.form["condition"])
    renovated = int(request.form["renovated"])

    # Create DataFrame
    new_data = pd.DataFrame({
         "city" : [city] ,
         "yr_built_bin" : [yr_built_bin] ,
         "sqft_basement": [sqft_basement],
         "sqft_above":[sqft_above],
         "total_rooms": [total_rooms],
         "floors": [floors],
         "view":[view],
         # "age":[age],
         "waterfront":[waterfront],
         "condition":[condition],
         "renovated":[renovated]
        
        
    })

    # Make prediction
    prediction = model.predict(new_data)[0]

    # Remove decimal
    prediction = int(prediction)

    # Send result back to webpage
    return render_template(
        "index.html",
        prediction=prediction
    )


if __name__ == "__main__":
    app.run(debug=True)
