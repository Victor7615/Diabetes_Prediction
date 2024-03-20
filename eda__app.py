import streamlit as st
import pandas as pd

# Data Viz Packages
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('Agg')
import seaborn as sns
import plotly.express as px

@st.cache_data         # for optimiztion and speed
def load_data(data):
    df=pd.read_csv(data)
    return df

def run_eda_app():
    st.subheader("EDA Section")
    data=load_data("diabetes_data_upload_clean.csv")
    data2=load_data("diabetes_data_upload.csv")
    
    st.write(data)

    submenu= st.sidebar.selectbox("SubMenu",["Describe","Plot"])

    if submenu=="Describe":
        st.dataframe(data)
        with st.expander("Data Type Summary"):
            st.dataframe(data.dtypes)
        with st.expander("Descriptive Summary"):
            st.dataframe(data.describe())
    else:
        st.subheader('Plot')

        #Layout 
        col1,col2 =st.columns([2,2])
        with col1:
            with st.expander("Dist_Plot of Gender"):
                #bar=px.bar(data2,x='Gender',y=data['gender'])
                #st.plotly_chart(bar)
                #fig =px.bar(data2,x="Gender",y="Polyuria")
                #st.plotly_chart(fig)
                fig=plt.figure()
                sns.countplot(x="gender",data=data)
                st.pyplot(fig)
        with col2:
            with st.expander("Dist_Plot of Obesity"):
                    
                fig=plt.figure()
                sns.countplot(x="obesity",data=data)
                st.pyplot(fig)
