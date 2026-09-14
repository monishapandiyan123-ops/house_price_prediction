# 🏠 House Price Prediction

An end-to-end machine learning project that predicts house prices based on property characteristics. The trained model is integrated into a Flask web application where users can enter property details and receive a predicted house price.

## 📌 Project Overview

House prices depend on several factors such as location, living area, number of bedrooms, property condition, construction year, and other property characteristics.

The goal of this project is to build a complete machine learning pipeline that takes raw housing data, performs data preprocessing and feature engineering, trains and evaluates multiple regression models, selects a suitable final model, and deploys it through a Flask web application.

## 🎯 Objective

* Analyze housing data and identify important factors affecting house prices.
* Perform data cleaning and preprocessing.
* Engineer meaningful features.
* Train and compare multiple regression models.
* Evaluate models using appropriate regression metrics.
* Select the best-performing model.
* Deploy the trained model using Flask.
* Provide house price predictions through a web interface.

## 📊 Dataset

The project uses a housing dataset containing property-related information such as:

* Location
* Living area
* Above-ground living area
* Basement area
* Bedrooms
* Bathrooms
* Floors
* Lot area
* Waterfront
* View
* Condition
* Year built
* Year renovated
* Other property characteristics

**Target variable:** `price`

## 🛠️ Technologies Used

* **Python**
* **Pandas** – Data manipulation and preprocessing
* **NumPy** – Numerical computation
* **Scikit-learn** – Machine learning
* **Flask** – Web application and model deployment
* **HTML** – Front-end interface
* **Git & GitHub** – Version control and project management

## 🔄 Machine Learning Workflow

```text
Raw Dataset
     ↓
Data Understanding
     ↓
Data Cleaning
     ↓
Exploratory Data Analysis
     ↓
Feature Engineering
     ↓
Feature Selection
     ↓
Train-Test Split
     ↓
Model Training
     ↓
Model Evaluation
     ↓
Model Comparison
     ↓
Final Model Selection
     ↓
Model Serialization
     ↓
Flask Deployment
     ↓
House Price Prediction
```

## 🧹 Data Preprocessing

The preprocessing stage included:

* Handling missing values
* Checking duplicate records
* Identifying invalid values
* Detecting and analyzing outliers
* Checking feature distributions
* Handling categorical variables
* Creating relevant derived features
* Preparing the final feature matrix for machine learning

## 🤖 Machine Learning Models

Multiple regression algorithms were evaluated to determine the most suitable model for the dataset.

Examples include:

* Linear Regression
* Tree-based regression models
* Gradient boosting models

Models were compared using:

* **MAE (Mean Absolute Error)**
* **RMSE (Root Mean Squared Error)**
* **R² Score**

## 📈 Model Evaluation

The models were evaluated on both training and testing data to understand their predictive performance and check for overfitting.

| Metric   | Purpose                                                    |
| -------- | ---------------------------------------------------------- |
| MAE      | Measures the average absolute prediction error             |
| RMSE     | Penalizes larger prediction errors                         |
| R² Score | Measures the proportion of variance explained by the model |

> The final model was selected based on its overall test-set performance and generalization ability.

## 💾 Model Saving

The final trained model was saved using `joblib` so that it could be loaded later by the Flask application without retraining the model.

## 🌐 Flask Web Application

The trained model is integrated into a Flask application.

Users can enter property information through the web interface, and the application sends the input to the trained model to generate the predicted house price.

### Application Flow

```text
User Input
    ↓
HTML Form
    ↓
Flask Application
    ↓
Input Preprocessing
    ↓
Trained ML Model
    ↓
Predicted House Price
    ↓
Result Displayed
```

## 📁 Project Structure

```text
house_price_prediction/
│
├── app.py
├── model.pkl
├── requirements.txt
├── README.md
├── .gitignore
│
├── templates/
│   └── index.html
│
└── static/
```

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/monishapandiyan123-ops/house_price_prediction.git
```

### 2. Navigate to the project directory

```bash
cd house_price_prediction
```

### 3. Create a virtual environment

```bash
python -m venv .venv
```

### 4. Activate the virtual environment

Windows:

```bash
.venv\Scripts\activate
```

### 5. Install dependencies

```bash
pip install -r requirements.txt
```

## ▶️ Run the Application

Run:

```bash
python app.py
```

Then open the local Flask URL displayed in the terminal.

## 📌 Results

The project successfully demonstrates an end-to-end machine learning workflow:

* Data preprocessing
* Exploratory data analysis
* Feature engineering
* Regression model development
* Model comparison
* Model evaluation
* Model serialization
* Flask integration
* User-based house price prediction

## 🚀 Future Improvements

* Deploy the application to a cloud platform.
* Improve the user interface.
* Add prediction confidence or uncertainty information.
* Add additional housing features.
* Experiment with advanced machine learning and ensemble techniques.
* Monitor model performance after deployment.
## 📈 Model Evaluation

Three regression models were compared using cross-validation:

| Model                 | CV R² Mean | CV R² Std | CV MAE Mean | CV RMSE Mean |
| --------------------- | ---------: | --------: | ----------: | -----------: |
| **Linear Regression** | **0.6830** |    0.0302 |      87,659 |      124,451 |
| XGBoost               |     0.6814 |    0.0166 |  **86,788** |      124,830 |
| LightGBM              |     0.6552 |    0.0236 |      91,475 |      129,747 |

Based on the overall cross-validation performance, **Linear Regression was selected as the baseline model** and further evaluated on the unseen test dataset.

### Final Linear Regression Performance

| Metric |   Training |    Testing |
| ------ | ---------: | ---------: |
| MAE    |  86,038.53 |  92,618.05 |
| RMSE   | 122,112.48 | 127,864.62 |
| R²     |     0.6970 | **0.7019** |

### Overfitting Check

* **Training R²:** 0.6970
* **Testing R²:** 0.7019
* **R² Gap:** -0.0049

The very small difference between training and testing R² indicates that the model generalizes well to unseen data and does not show significant overfitting.

The final Linear Regression model achieved an **R² score of 0.7019**, meaning it explains approximately **70.2% of the variation in house prices** on the unseen test dataset.

### Final Model Selection

**Final Model: Linear Regression**

The model was selected based on its cross-validation performance, final test performance, and good generalization between training and testing data.


## 👩‍💻 Author

**Monisha Pandiyan**

Data Science | Machine Learning | Python

---

⭐ If you find this project useful, consider giving the repository a star.
