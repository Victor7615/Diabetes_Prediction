import streamlit as st
from eda__app import run_eda_app
from Ml__app import run_ml
import streamlit.components.v1 as stc  # for running CSS and HTML in streamlit


html_temp= """
        <div style="background-color:#4F3BA2; padding:10px; border-radius:10px;">
        <h1 style="color:white; text-align:center;"> Early stage DM Risk Data App</h1>  
        <h4 style="color:white; text-align:center;">Diabetes Mellitus </h4>
        </div>
           """

def main():
    #st.title("ML web app with Streamlit")
    stc.html(html_temp)

    menu =["Home","EDA","ML","About"]
    choice=st.sidebar.selectbox("Menu",menu)
    if choice=="Home":
        st.subheader("Home")
        st.write(
        """
         ### Early Stage Diabetes risk predictor App
         This dataset contains the sign and symptoms data of newly diabetic or would be diabetic patient.
        ### Datasource
            -https://archieve.ics.uci.edu/ml/datasets/Early+stage+diabetes+risk+prediction+dataset.
        ### App Content
            -EDA Section: Exploratory Data Analysis of Data
            -ML Section: ML Predictor App
        """)
    elif choice=="EDA":
        run_eda_app()
       
    elif choice=="ML":
        run_ml()
        
        
    else:
        st.subheader("About")
        st.text("""  App By Victor Emuchay
        
- 💡 Our Machine learning helps detect early signs of type 2 diabetes (Diabetes Mellitus 2,DM 2).
- 📊 Researchers predict DM 2 using statistics and machine learning.
- 📉 Age, gender, family history of DM, and high blood sugar levels are crucial factors in DM 2.
- 🔄 Family history of DM, age, and high blood pressure increase DM 2 risk.
- 📈 Maintaining normal blood sugar levels is essential for preventing DM 2.
- 🧪 Our computer program accurately predicts DM 2 risks with 89% using logistic Regression Model.
- 🩺 Smoking and activity have minimal impact on DM 2 risk.
- 🤖 Computers learning from data can potentially identify DM 2 risks early. """)

if __name__== '__main__':

    main()
