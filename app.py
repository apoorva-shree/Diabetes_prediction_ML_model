# -*- coding: utf-8 -*-
"""
Created on Thu May 28 12:04:34 2026

@author: HP
"""

import numpy as np
import pickle
import streamlit as st

loaded_model=pickle.load(open('C:/Users/HP/Documents/DATA SETS FOR ML MODELS/trained_model.sav','rb'))

#creating a function for diabtes predition
def diabetes_prediction(input_data):
    input_data=(0,118,84,47,230,45.8,0.551,31)

    #converting input data to numpy array
    input_data_as_numpy_array=np.asarray(input_data)

    #reshaping the array as we need to tell the model that we need prediction just for one array
    input_data_reshaped=input_data_as_numpy_array.reshape(1,-1)

    prediction=loaded_model.predict(input_data_reshaped)
    print(prediction)

    if(prediction[0]==0):
      print("The person is not diabetic")
    else:
      print("The person is diabetic")
      
def main():
    
    #giving a title
    st.title('Diabetes pridiction web app')
    
    #getting input data from user
    #Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age
    
    Pregnancies=st.text_input('Number of pregnancies')
    Glucose=st.text_input('Glucose level')
    BloodPressure=st.text_input('Bloodpressur level')
    SkinThickness=st.text_input('SkinThicknes:')
    Insulin=st.text_input('Insulin level')
    BMI=st.text_input('BMI level')
    DiabetesPedigreeFunction=st.text_input('DiabetesPedigreeFunction level')
    Age=st.text_input('Age')
    
    # code for prediction
    diagonsis=''
    
    #creating button for prediction
    if st.button('Diabetes test result'):
        diagonsis=diabetes_prediction([ Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age])
        
    
    st.success(diagonsis)
    
    
if __name__=='__main__':
    main()
    
    
    
