import streamlit as st
import joblib

# 모델 불러오기
vectorizer, model = joblib.load("freq.pkl")

# 제목
st.title("외국어 문장 판별")

# 입력 안내
st.write("외국어 입력 (입력후 CTRL + ENTER)")

# 문장 입력창
text = st.text_area("")

# 입력이 있으면 자동 분석
if text:
    X = vectorizer.transform([text])
    pred = model.predict(X)[0]

    st.write(pred)
