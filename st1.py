import streamlit as st

a = st.number_input("Enter a number:")
b = st.number_input("Enter another number:")

if st.button("Add"):
    st.write("Answer:", a + b)

if st.button("Subtract"):
    st.write("Answer:", a - b)

if st.button("Multiply"):
    st.write("Answer:", a * b)

if st.button("Divide"):
    st.write("Answer:", a / b)