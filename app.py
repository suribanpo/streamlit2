import streamlit as st

st.title("Hello 숩숩!😊👍")
name = st.text_input("이름을 입력해주세요. ")
if name !="":
    st.write(f"{name}님! 저의 페이지에 오신 것을 환영합니다. ")

st.balloons()