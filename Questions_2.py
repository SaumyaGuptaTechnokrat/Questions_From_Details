import streamlit as st
import pandas as pd

st.title("QUESTION PAGE")

st.header("Scroll Down to Submit Answer")

name = st.text_input("Enter Your Name:")
id_1 = st.number_input("Enter Phone Number: ")    
button_1 = st.button("Submit")
if button_1:
    st.header( f'Hello!! {name}.So Your Question is as below:- ')
df = pd.read_csv("C_4.csv")

for i in range(0,34):
    if name==df.iloc[i].NAME_OF_PARTICIPANTS and id_1==df.iloc[i].PHONE_NO:
        st.header(df.iloc[i].QUESTIONS)
st.header('*Compulsory Submissions:- ')
st.header("Circuit, Explain the final Output of the circuit, Video Explanation (if Possible), Uses of Circuit")
st.header("*Submit Your Answers Here:- ")
st.header("https://forms.gle/RhiZNk7u8nqnXL999")
