import streamlit as st
import pickle
model=pickle.load(open("modelr.pkl",'rb'))
scaler=pickle.load(open("scaler.pkl",'rb'))
studyhour=st.number_input("Sleep Hour",min_value=0,max_value=1,step=0.01)
sleephour=st.number_input("Study Hour",min_value=0,max_value=1,step=0.01)
attendance=st.number_input("Attendance",min_value=0,max_value=1,step=0.01)
final=st.number_input("Attendance",min_value=0,max_value=100)
partcipa
