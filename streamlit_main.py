import streamlit as st
import joblib

model = joblib.load("freq.pkl")

st.title("외국어 문장 판별")
st.write("외국어 입력 (입력후 CTRL + ENTER)")

text = st.text_area("외국어 문장 입력", label_visibility="collapsed")

if text:
    pred = model.predict([text])[0]
    st.write(pred))
