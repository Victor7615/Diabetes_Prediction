# Diabetes_Prediction

# Diabetes Prediction Model

This repository contains code for building a machine learning model to predict diabetes based on certain features. The dataset used for training and testing the model is `diabetes_data_upload.csv`.

## Contents

1. **Introduction**: 
   - This project aims to develop a predictive model for diabetes using machine learning techniques.
   
2. **Setup**: 
   - Ensure you have all necessary packages installed, as mentioned in `requirements.txt`.
   - The dataset `diabetes_data_upload.csv` should be available in the appropriate directory.
   
3. **Exploratory Data Analysis (EDA)**: 
   - The initial steps involve exploring the dataset, checking for missing values, and encoding categorical variables.
   - Visualization tools like Matplotlib, Seaborn, and Plotly Express are utilized for data exploration.

4. **Feature Engineering and Selection**: 
   - Features are selected using techniques like SelectKBest and ExtraTreesClassifier to identify the most significant predictors of diabetes.

5. **Model Development**: 
   - Various classification models such as Logistic Regression, Random Forest Classifier, and Decision Tree Classifier are trained and evaluated.
   - Model accuracy is assessed using metrics like accuracy score.

6. **Model Deployment**: 
   - The trained Logistic Regression model is saved using Joblib for future use.
   - Instructions for loading the saved model are provided.
   - The model is deployed to a web application using Streamlit.

## Instructions for Use

1. **Clone the Repository**: 
   ```
   git clone https://github.com/your_username/diabetes-prediction.git
   ```

2. **Install Dependencies**: 
   ```
   pip install -r requirements.txt
   ```

3. **Run the Notebook**: 
   - Open and run the Jupyter Notebook `diabetes_prediction.ipynb`.
   - Follow the step-by-step instructions to explore the dataset, build the model, and evaluate its performance.

4. **Model Deployment**: 
   - Load the saved Logistic Regression model (`Logistic_regression_diabetes_14_03_2024.pkl`) using Joblib for predictions.
   - Example code for making predictions is provided in the notebook.
   - The model is deployed to a web application using Streamlit. Instructions for running the web app are provided in the `app/README.md` file.

## Contributor
- Victor Emuchay

## Acknowledgments
- ([Data Set Source](https://archive.ics.uci.edu/dataset/529/early+stage+diabetes+risk+prediction+dataset) [DataSet Source]
- Other Resources(sklearn Library,Pandas,Numpy,Matploblib,Seaborn,Plotly,Joblib)

