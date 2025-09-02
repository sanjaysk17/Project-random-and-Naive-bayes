import streamlit as st
import pickle
import numpy as np
model = pickle.load(open("modelr.pkl",'rb'))
st.title("Student Performance Predictor")
study_hours=st.number_input("Study Hours per Week",min_value=0.0,max_value=100.0,step=1.0)
sleep_hours=st.number_input("Sleep Hours per Day",min_value=0.0,max_value=24.0,step=0.5)
attendance=st.number_input("Attendance Percentage",min_value=0.0,max_value=100.0,step=1.0)
assignments=st.number_input("Assignments Completed",min_value=0,max_value=50, step=1)
if st.button("Predict"):
    data=np.array([[study_hours,sleep_hours,attendance,assignments]])
    prediction = model.predict(data)[0]
    if prediction == 1:
        st.success("Pass")
    else:
        st.error("Fail")