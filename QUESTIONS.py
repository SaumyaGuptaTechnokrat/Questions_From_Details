import streamlit as st
import pandas as pd

st.title("REGISTRATION PAGE")




name = st.text_input("Enter Your Name:")
id_1 = st.number_input("Enter Phone Number: ")    
button_1 = st.button("Submit")
if button_1:
    st.header( f'Hello!! {name}.So Your Question is as below:- ')
df = pd.read_csv("Registration - Sheet1.csv")

for i in range(0,4):
    if name==df.iloc[i].Name and id_1==df.iloc[i].Unique_Id:
        st.header(df.iloc[i].Question)