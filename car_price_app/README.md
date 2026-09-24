# 🚗 PredictCarPrice

A machine learning application that predicts the price of a car based on information such as brand, model, year, engine size, fuel type, transmission, mileage, number of doors, and number of previous owners.

The project uses **Python, Pandas, Scikit-learn, Joblib, and Streamlit** to provide a simple web interface for making car price predictions.

## 📌 Features

* Select a car brand directly from the dataset
* Select a car model based on the selected brand
* Enter the car's year
* Enter engine size
* Select fuel type
* Select transmission
* Enter mileage
* Enter number of doors
* Enter number of previous owners
* Get a predicted car price using a trained machine learning model

The available brands, models, fuel types, and transmission types are loaded directly from the CSV dataset. This means the Streamlit application does not contain hard-coded lists of car manufacturers or models.

## 🧠 Machine Learning

The application uses a trained **Linear Regression** model to predict the price of a car.

The trained model is stored as:

```text
car_price_linear_regression.joblib
```

The application loads the model using Joblib:

```python
model = joblib.load("car_price_linear_regression.joblib")
```

The user's input is then placed into a Pandas DataFrame and passed to the trained model:

```python
predicted_price = model.predict(new_car)
```

## 📊 Dataset

The application uses:

```text
car_price_dataset.csv
```

The dataset contains information about cars including:

| Feature        | Description               |
| -------------- | ------------------------- |
| `Brand`        | Car manufacturer          |
| `Model`        | Car model                 |
| `Year`         | Model year                |
| `Engine_Size`  | Engine size               |
| `Fuel_Type`    | Type of fuel              |
| `Transmission` | Transmission type         |
| `Mileage`      | Mileage                   |
| `Doors`        | Number of doors           |
| `Owner_Count`  | Number of previous owners |
| `Price`        | Car price                 |

The application reads the dataset using Pandas:

```python
df = pd.read_csv("car_price_dataset.csv", sep=";")
```

## 🖥️ Application

The application is built with **Streamlit** and provides a simple user interface where users can enter the characteristics of a car and receive a predicted price.

Example workflow:

```text
User input
    ↓
Streamlit
    ↓
Pandas DataFrame
    ↓
Trained Linear Regression model
    ↓
Predicted car price
```

## 🛠️ Technologies

* **Python**
* **Pandas** – data loading and manipulation
* **Scikit-learn** – machine learning
* **Joblib** – saving and loading the trained model
* **Streamlit** – web application
* **Git / GitHub** – version control

## 📁 Project Structure

```text
PredictCarPrice/
│
├── app.py
├── car_price_dataset.csv
├── car_price_linear_regression.joblib
├── requirements.txt
├── .gitignore
└── README.md
```

### File descriptions

**`app.py`**

The main Streamlit application. It loads the dataset and trained model, creates the user interface, collects user input, and generates predictions.

**`car_price_dataset.csv`**

The dataset used by the application to provide available car information and feature ranges.

**`car_price_linear_regression.joblib`**

The trained machine learning model used to predict car prices.

**`requirements.txt`**

Contains the Python dependencies required to run the application.

**`.gitignore`**

Specifies files and folders that should not be committed to Git, such as the Python virtual environment and cache files.

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone git@github.com:Grevendev/PredictCarPrice.git
```

Then navigate into the project:

```bash
cd PredictCarPrice
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

### 3. Activate the virtual environment

On Windows Git Bash:

```bash
source venv/Scripts/activate
```

Or in Windows Command Prompt:

```cmd
venv\Scripts\activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

### 5. Start the application

```bash
streamlit run app.py
```

Streamlit will start a local web server and provide a URL that can be opened in your browser.

## 🔮 Future Improvements

Possible improvements for the project include:

* Experimenting with additional machine learning algorithms
* Comparing Linear Regression with models such as Random Forest and Gradient Boosting
* Improving model evaluation
* Adding visualizations of the dataset
* Displaying model performance metrics
* Improving the user interface
* Adding additional car features
* Deploying the application online

## 🎯 Purpose

This project was created as a practical machine learning project to combine **data processing, machine learning, model persistence, and application development** into a working Python application.

The goal is not only to train a machine learning model, but also to make the model usable through a simple web application.
