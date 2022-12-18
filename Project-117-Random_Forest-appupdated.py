# -*- coding: utf-8 -*-
"""
Created on Fri May 27 20:39 2022

"""

import pandas as pd
import numpy as np
import streamlit as st 
from pickle import dump
from pickle import load
import pickle








loaded_model = load(open('P-117-Random_Forest.sav', 'rb'))














# creating a function for Prediction

def Potability_prediction(input_data):
    
    
    # changing the input_data to numpy array
    input_data_as_numpy_array = np.asarray(input_data)

    # reshape the array as we are predicting for one instance
    input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

    prediction = loaded_model.predict(input_data_reshaped)
    print(prediction)

    if (prediction == 1):
      return 'YES'
    else:
      return 'NO'
  


def main():
    
    
    #giving a title
    st.title('Random Forest')
    
    
    # getting the input data from the user
    
    
    number1 = st.number_input('Insert  Ph')
    number2 = st.number_input('Insert  Hardness')
    number3 = st.number_input('Insert  Solids')
    number4 = st.number_input('Insert  Chloramines')
    number5 = st.number_input('Insert  Sulfate')
    number6 = st.number_input('Insert  Conductivity')
    number7 = st.number_input('Insert  Organic_carbon')
    number8 = st.number_input('Insert  Trihalomethanes')
    number9 = st.number_input('Insert  Turbidity')
    
    
#     # code for Prediction
    diagnosis = ''
    
    # creating a button for Prediction
    
    if st.button('Potability Test Result'):
        diagnosis = Potability_prediction([number1,number2,number3,number4,number5,number6,number7,number8,number9])
        
        
    st.success(diagnosis)
    
    
    
    
    
if __name__ == '__main__':
    main()
    
    
    
    
    
