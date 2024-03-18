# -*- coding: utf-8 -*-
"""Diabetic_prediction.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1QSNgKzGT_cIiTIuclsLX8n9B-XWTfs1s
"""

# Load EDA Packages
import pandas as pd
import numpy as np

# Load Viz Packages
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

# Load Machine Learning Packages
import sklearn
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import DecisionTreeClassifier

# For Metrics

from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split

# Read Dataset
df=pd.read_csv("/content/drive/MyDrive/diabetes_data_upload.csv")
df.head()

# Check for shape of Data Set

df.shape



# Check for Columns
df.columns

# Check for Missing Values

df.isnull().sum()

# Converting and Cleaning up columns
df.columns.str.lower().str.replace(' ','_')

df.columns=df.columns.str.lower().str.replace(' ','_')

df.columns

# Encode the dataset
from sklearn.preprocessing import LabelEncoder

objList=df.select_dtypes(include ="object").columns

objList

# selecting all columns excluding  age,gender and class as they are of different charecteristics i.e All others are Yes or No while Gender and Class have different categories.
columns_to_label_encode=['polyuria', 'polydipsia', 'sudden_weight_loss', 'weakness',
       'polyphagia', 'genital_thrush', 'visual_blurring', 'itching',
       'irritability', 'delayed_healing', 'partial_paresis',
       'muscle_stiffness', 'alopecia', 'obesity']

# instantiate Label Encoding
LE=LabelEncoder()

# Encode every column except age,gender and class

for col in columns_to_label_encode:
  df[col]=LE.fit_transform(df[col].astype(str))

df.dtypes

# List initial Classes
print(LE.classes_)

# Method 2 using custom function for encoding gender and class columns

#gender_map={'Female':0,'Male':1}
#target_label_map={'Negative':0,'Positive':1}

#df['gender'].unique()

#df['gender']=df['gender'].map(gender_map)

#df['class'].unique()

#df['class']=df['class'].map(target_label_map)



# Label Encoding for gender
df['gender']=LE.fit_transform(df['gender'])

# Label Encoding for class
df['class']=LE.fit_transform(df['class'])

# checking our data types after encoding
df.dtypes

df.head()

# recheck info
df.info()

# value count per class
df['class'].value_counts()

# Plot of Distribution of data per class/label

px.bar(df,x="class")

# Plot of Distribution of data per class/label
plt.figure(figsize=(10,5))
plt.title("Plot of Distribution of Data per Class")
sns.countplot(x='class',data=df)
plt.show()

# Feature Engineering and Selection

from sklearn.feature_selection import SelectKBest,chi2,RFE
from sklearn.ensemble import ExtraTreesClassifier

df.columns

x=df[['age', 'gender', 'polyuria', 'polydipsia', 'sudden_weight_loss',
       'weakness', 'polyphagia', 'genital_thrush', 'visual_blurring',
       'itching', 'irritability', 'delayed_healing', 'partial_paresis',
       'muscle_stiffness', 'alopecia', 'obesity']]

y=df['class']

# Find the best features using SelectkBest
skb= SelectKBest(score_func=chi2,k=10)
best_feature_fit=skb.fit(x,y)

# Mapping to features name

feature_scores=pd.DataFrame(best_feature_fit.scores_,columns=['feature_score'])

feature_scores

# providing proper labeling for the feature scores
feature_column_name=pd.DataFrame(x.columns,columns=['feature_names'])
best_feat_df=pd.concat([feature_scores,feature_column_name],axis=1)

best_feat_df

best_feat_df.nlargest(10,"feature_score")

# ExtraTreeClassifier

et_clf=ExtraTreesClassifier()
et_clf.fit(x,y)

print(et_clf.feature_importances_)

# using column names as index to match the series of feature selection attributes
feature_importance_df=pd.Series(et_clf.feature_importances_,index=x.columns)
feature_importance_df

# Identifying Top 12 feature importance with a horizontal bar chart
feature_importance_df.nlargest(12).plot(kind='barh')

# Model Development

# Split Dataset into 2

x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.3,random_state=7)

#shape of data set

print("Original data ",df.shape)
print("train  data  ",x_train.shape)
print("Test data  ",x_test.shape)

#Using logistic regression Estimator  to build model

lr_model=LogisticRegression()
lr_model.fit(x_train,y_train)

# Check model Accuracy

# Method 1

lr_model.score(x_test,y_test)

# Check model prediction

y_pred=lr_model.predict(x_test)

y_pred

# test with other classification models

# Create a list of features
#features = [35, 1, 1, 1, 0, 0, 1, 0, 1, 1, 0, 0, 0, 1, 0, 1]

# Make a prediction using the list of features
#z_pred = lr_model.predict([features])
#if z_pred==1:
#  print("Sorry!You have Diabetes")
#else:
#  print("Congratulations!You dont have Diabetes")



import joblib

#Check for  Joblib Version
print('Joblib',joblib.__version__)

# Save LR Model
model_file_dt=open("Logistic_regression_diabetes_14_03_2024.pkl","wb")
joblib.dump(lr_model,model_file_dt) # putting/writing  the logistic regression model into variable file,model_file_dt,with file name,Logistic_regression_diabetes_14_03_2024.pkl
model_file_dt.close()