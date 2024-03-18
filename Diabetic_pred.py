import numpy as np
import streamlit as st


import pickle

import joblib

st.title("Diabetic Prediction ")
    

# Path to your saved model
model_path = "C:\\Users\\USER\\Desktop\\Streamlit\\Diabetic_prediction\\Logistic_regression_diabetes_14_03_2024.pkl"

# Load the model using joblib
try:
    model = joblib.load(model_path)
    print("Model loaded successfully!")
except FileNotFoundError:
    print(f"Model not found at {model_path}. Please ensure the file exists.")
    exit(1)

# Import LabelEncoder (assuming you used it in your training script)
from sklearn.preprocessing import LabelEncoder



# Get user input from Streamlit elements
Age = st.number_input("Age",step=1)
Gender = st.selectbox("Gender", ("Male", "Female"))

Polyuria = st.selectbox("Polyuria", (0, 1))
Polydipsia = st.selectbox("Polydipsia", (0, 1))
Sudden_weight_loss = st.selectbox("Sudden Weight Loss", (0, 1))
Weakness = st.selectbox("Weakness", (0, 1))
Polyphagia = st.selectbox("Polyphagia", (0, 1))
Genital_thrush = st.selectbox("Genital Thrush", (0, 1))
Visual_blurring = st.selectbox("Visual Blurring", (0, 1))
Itching = st.selectbox("Itching", (0, 1))
Irritability = st.selectbox("Irritability", (0, 1))
Delayed_healing = st.selectbox("Delayed Healing", (0, 1))
Partial_paresis = st.selectbox("Partial Paresis", (0, 1))
Muscle_stiffness = st.selectbox("Muscle Stiffness", (0, 1))
Alopecia = st.selectbox("Alopecia", (0, 1))
Obesity = st.selectbox("Obesity", (0, 1))

# Assuming you have the LabelEncoder object (`LE`) from your training script
# Instantiate and fit LabelEncoder for Gender if not already done,this is to convert your drop down numeric values after been parsed as input by the user.
LE_gender = LabelEncoder()
LE_gender.fit(["Male", "Female"])

# Encode Gender
encoded_gender = LE_gender.transform([Gender])[0]

# Make prediction
user_data = [Age, encoded_gender, Polyuria, Polydipsia, Sudden_weight_loss, Weakness, Polyphagia, Genital_thrush, Visual_blurring, Itching, Irritability, Delayed_healing, Partial_paresis, Muscle_stiffness, Alopecia, Obesity]

prediction = model.predict([user_data])
if st.button('Predict'):
        prediction = model.predict([user_data])
       
        if prediction == 1:
             
            st.warning("You might have Diabetes. Please consult a doctor!")
        else:

            st.success("You likely don't have Diabetes.")


# ... display prediction results ...




#model =pickle.load(open('Logistic_regression_diabetes_14_03_2024.pkl','rb'))
#def main():
    #st.title("Diabetic Prediction Solution")
    

    # creating input Variables

    #Age =st.text_input('age')
    #Gender=st.text_input('gender')
    #Polyuria=st.text_input('polyuria')
    #Polydipsia=st.text_input('polydipsia')
    #sudden_weight_loss=st.text_input('sudden_weight_loss')
    #Weakness=st.text_input('weakness')
    #Polyphagia=st.text_input('polyphagia')
    #Genital_thrush=st.text_input('genital_thrush')
    #Visual_blurring=st.text_input('visual_blurring')
    #Itching=st.text_input('itching')
    #irritability=st.text_input('irritability')
    #Delayed_healing=st.text_input('delayed_healing')
    #Partial_paresis=st.text_input('partial_paresis')
    #Muscle_stiffness=st.text_input('muscle_stiffness')
    #Alopecia=st.text_input('alopecia')
    #Obesity=st.text_input('obesity')
    

    # prediction
   # if st.button('Predict'):
       # makeprediction=model.predict([[Age,Gender,Polyuria,Polydipsia,sudden_weight_loss,Weakness,Polyphagia,Genital_thrush,Visual_blurring,Itching,irritability,Delayed_healing,Partial_paresis,Muscle_stiffness,Alopecia,Obesity]])

         
        #if makeprediction==1:
             
           # st.warning("Sorry!you have Diabetes")
        #else:
           #  st.success("Congratution! You dont have diabetes")

#if __name__=='__main__':

#    main()

#'C:\\Users\\USER\\Desktop\\Streamlit\\Diabetic_prediction\\Logistic_regression_diabetes_14_03_2024.pkl','rb'