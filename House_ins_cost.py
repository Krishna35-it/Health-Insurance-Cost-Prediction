import streamlit as st
import pandas as pd
import numpy as np
import pickle

#Loading the trained model
with open('Insurance_Cost_Prediction_GB_Model.pkl','rb') as file:
    model = pickle.load(file)

st.title("House Insurance Cost Prediction App")
st.write("Fill in the details below to predict the medical insurance cost.")

#Input fields
age = st.slider("Age",18,100,30)
sex = st.selectbox("Sex",["male","female"])
bmi = st.number_input("BMI (Body Mass Index)",min_value=10.0,max_value=50.0,step=0.1)
children = st.slider("Number of Children",0,5,0)
smoker = st.selectbox("Smoker",["yes","no"])
region = st.selectbox("Region",["southwest","southeast","northwest","northeast"])

#Mapping categorical values as per the trained model
sex = 1 if sex == "male" else 0 
smoker = 1 if smoker == "yes" else 0
region_map = {"southwest":1,"southeast":2,"northwest":3,"northeast":4}
region = region_map[region]

#Creating an Input array
input_data = np.array([[age,sex,bmi,children,smoker,region]])

#Prediction
if st.button("Predict Insurance Cost"):
    prediction = model.predict(input_data)[0]
    st.success(f"Estimated Insurance Cost:Rs.{prediction:,.2f}")