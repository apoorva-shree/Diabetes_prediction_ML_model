Diabetes Prediction using Machine Learning

This project uses Machine Learning to predict whether a person is diabetic or not based on medical attributes. The model is built using Python and trained with the Support Vector Machine (SVM) algorithm.

📌 Project Overview

The notebook performs the complete Machine Learning workflow:

Importing required libraries
Data collection and analysis
Data preprocessing
Feature standardization
Train-test splitting
Model training using SVM
Model evaluation using accuracy score
Building a predictive system


📂 Dataset Information

The dataset contains medical details of patients such as:

Pregnancies
Glucose Level
Blood Pressure
Skin Thickness
Insulin
BMI
Diabetes Pedigree Function
Age
Outcome (0 = Non-Diabetic, 1 = Diabetic)


🛠️ Technologies Used
Python
NumPy
Pandas
Scikit-learn
Google Colab / Jupyter Notebook
🤖 Machine Learning Algorithm



The model uses:

Support Vector Machine (SVM)

with a linear kernel for classification.



⚙️ Steps Performed
1. Importing Dependencies

Libraries like NumPy, Pandas, and Scikit-learn are imported.

2. Data Collection & Analysis

The diabetes dataset is loaded and analyzed using:

head()
describe()
value_counts()
groupby()

3. Data Preprocessing

Features and labels are separated.
Data is standardized using StandardScaler.

4. Train-Test Split

Dataset is divided into training and testing data using train_test_split().

5. Model Training

The SVM classifier is trained on the training dataset.

6. Model Evaluation

Accuracy score is calculated for:

Training data
Testing data

7. Predictive System

The model can take custom input data and predict whether a person is diabetic or non-diabetic.



📊 Model Performance

The project evaluates the model using accuracy score on both training and testing datasets.


📁 Project Structure

├── Diabetes_ML(2nd).ipynb
├── diabetes.csv
└── README.md


🎯 Future Improvements

Improve model accuracy using advanced algorithms
Add data visualization
Deploy the model as a web application
Create a user-friendly interface


👨‍💻 Author

Apoorva Shree