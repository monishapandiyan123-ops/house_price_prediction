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

Three regression models were compared using 5-fold cross-validation:

| **Model**     | **CV R² Mean** | **CV R² Std** | **CV MAE Mean** | **CV RMSE Mean** |
| ------------- | -------------: | ------------: | --------------: | ---------------: |
| **CatBoost**  |     **0.7002** |        0.0107 |      **86,187** |      **123,726** |
| XGBoost       |         0.6843 |        0.0053 |          87,456 |          126,965 |
| Random Forest |         0.6605 |        0.0110 |          92,188 |          131,666 |

Based on the overall cross-validation performance, **CatBoost was selected as the best baseline model** and further evaluated on the unseen test dataset.

### CatBoost Hyperparameter Tuning

CatBoost was further optimized using hyperparameter tuning with 5-fold cross-validation.

**Best Parameters:**

* `iterations`: 800
* `learning_rate`: 0.03
* `depth`: 5
* `l2_leaf_reg`: 5
* `random_strength`: 5
* `bagging_temperature`: 2

**Best CV R²:** **0.6991**

### Final CatBoost Performance

| **Metric** | **Training** |    **Testing** |
| ---------- | -----------: | -------------: |
| MAE        |    76,429.39 |  **85,673.10** |
| RMSE       |   108,235.12 | **122,154.59** |
| R²         |       0.7707 |     **0.7047** |

The final CatBoost model achieved a **testing R² score of 0.7047**, meaning that the model explains approximately **70.5% of the variation in house prices** on the unseen test dataset.

### Overfitting Check

* **Training R²:** 0.7707
* **Testing R²:** 0.7047
* **R² Gap:** 0.0661

The training R² is higher than the testing R², resulting in an R² gap of approximately **6.6 percentage points**. This indicates **some degree of overfitting**, although the model still maintains a testing R² of approximately 70.5% on unseen data.

The relatively close cross-validation score (**0.6991**) and testing score (**0.7047**) also indicate that the model's performance is reasonably consistent with its validation performance.

### Final Model Selection

**Final Model: CatBoost Regressor**

CatBoost was selected based on its cross-validation performance and final test performance. It achieved the highest mean CV R² (**0.7002**) among the compared baseline models and achieved a final testing R² of **0.7047**.

The model was then used as the final model for the house price prediction application.



## 👩‍💻 Author

**Monisha Pandiyan**

Data Science | Machine Learning | Python

---

⭐ If you find this project useful, consider giving the repository a star.
