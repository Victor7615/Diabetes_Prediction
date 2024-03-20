import numpy as np
import streamlit as st


import pickle

import joblib

st.title("Diabetic Prediction ")
    
attrib_info="""

### Attribute Information:
- Age 1.20-65		
- Sex 1. Male, 2.Female		
- Polyuria 1.Yes, 2.No.		
- Polydipsia 1.Yes, 2.No.		
- sudden weight loss 1.Yes, 2.No.		
- weakness 1.Yes, 2.No.		
- Polyphagia 1.Yes, 2.No.		
- Genital thrush 1.Yes, 2.No.		
- visual blurring 1.Yes, 2.No.		
- Itching 1.Yes, 2.No.		
- Irritability 1.Yes, 2.No.		
- delayed healing 1.Yes, 2.No.		
- partial paresis 1.Yes, 2.No.		
- muscle stiffness 1.Yes, 2.No.		
- Alopecia 1.Yes, 2.No.		
- Obesity 1.Yes, 2.No.		
- Class 1.Positive, 2.Negative.		


"""
st.expander(attrib_info)
def run_ml():
# Path to your saved model
    model_path = "C:\\Users\\USER\\Desktop\\Streamlit\\Diabetic_prediction\\Logistic_regression_diabetes_14_03_2024.pkl"

# Load the model using joblib
    try:
        model = joblib.load(model_path)
        print("Model loaded successfully!")
    except FileNotFoundError:
        print(f"Model not found at {model_path}. Please ensure the file exists.")
        exit(1)
    with st.expander("Attribute info"):
        st.markdown(attrib_info,unsafe_allow_html=True)

# Import LabelEncoder (assuming you used it in your training script)
    from sklearn.preprocessing import LabelEncoder



# Get user input from Streamlit elements
    col1, col2 = st.columns(2)
    with col1:
        Age = st.number_input("Age",step=1,min_value=10,max_value=65)
        Gender = st.selectbox("Gender", ("Male", "Female"))

        Polyuria = st.selectbox("Polyuria", ('Yes', 'No'))
        Polydipsia = st.selectbox("Polydipsia", ('Yes', 'No'))
        Sudden_weight_loss = st.selectbox("Sudden Weight Loss", ('Yes', 'No'))
        Weakness = st.selectbox("Weakness", ('Yes', 'No'))
        Polyphagia = st.selectbox("Polyphagia", ('Yes', 'No'))
        Genital_thrush = st.selectbox("Genital Thrush", ('Yes', 'No'))
    with col2:   
        Visual_blurring = st.selectbox("Visual Blurring", ('Yes', 'No'))
        Itching = st.selectbox("Itching", ('Yes', 'No'))
        Irritability = st.selectbox("Irritability", ('Yes', 'No'))
        Delayed_healing = st.selectbox("Delayed Healing", ('Yes', 'No'))
        Partial_paresis = st.selectbox("Partial Paresis", ('Yes', 'No'))
        Muscle_stiffness = st.selectbox("Muscle Stiffness", ('Yes', 'No'))
        Alopecia = st.selectbox("Alopecia", ('Yes', 'No'))
        Obesity = st.selectbox("Obesity", ('Yes', 'No'))

# Assuming you have the LabelEncoder object (`LE`) from your training script
# Instantiate and fit LabelEncoder for Gender if not already done,this is to convert your drop down numeric values after been parsed as input by the user.
    LE_gender = LabelEncoder()
    LE_gen = LabelEncoder()
    LE_gen.fit(["Male", "Female"])
    LE_gender.fit(["Yes", "No"])
    
# Encode Gender
    
    encoded_gen = LE_gen.transform([Gender])[0]
    encoded_polyuria = LE_gender.transform([Polyuria])[0]
    encoded_polydipsia = LE_gender.transform([Polydipsia])[0]
    encoded_sudd = LE_gender.transform([Sudden_weight_loss])[0]
    encoded_weakness = LE_gender.transform([Weakness])[0]
    encoded_polyphagia = LE_gender.transform([Polyphagia])[0]
    encoded_Genital = LE_gender.transform([Genital_thrush])[0]
    encoded_visual = LE_gender.transform([Visual_blurring])[0]
    encoded_Itch = LE_gender.transform([Itching])[0]
    encoded_irr = LE_gender.transform([Irritability])[0]
    encoded_delayed = LE_gender.transform([Delayed_healing])[0]
    encoded_partial = LE_gender.transform([Partial_paresis])[0]
    encoded_Muscle = LE_gender.transform([Muscle_stiffness])[0]
    encoded_Alopecia = LE_gender.transform([Alopecia])[0]
    encoded_Obesity = LE_gender.transform([Obesity])[0]
    

# Make prediction
    user_data = [Age, encoded_gen, encoded_polyuria, encoded_polydipsia, encoded_sudd, encoded_weakness,
                  encoded_polyphagia, encoded_Genital, encoded_visual, encoded_Itch, encoded_irr, 
                  encoded_delayed, encoded_partial, encoded_Muscle, encoded_Alopecia, encoded_Obesity]

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