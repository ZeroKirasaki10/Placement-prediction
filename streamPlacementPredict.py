import streamlit as sl
import pickle
import numpy as np

with open(r'C:\Users\HP\OneDrive\Desktop\streamlit\code\model (1).pkl','rb') as f:
    model = pickle.load(f)


sl.title('Placement Prediction App')


cgpa = sl.number_input('Enter CGPA:')
iq = sl.number_input('Enter IQ:')


input_data = np.array([cgpa, iq]).reshape(1, -1)
prediction = model.predict(input_data)[0]


if prediction == 1:
    sl.success('This student is likely to be placed.')
else:
    sl.error('This student is not likely to be placed.')