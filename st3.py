import streamlit as st

number = st.number_input("Enter a number:", step=1)

if st.button("Show Table"):
    for i in range(1, 11):
        st.write(f"{number} x {i} = {number * i}")  

if st.button("Show Square"):
    st.write(f"The square of {number} is {number ** 2}")

if st.button("Show Cube"):
    st.write(f"The cube of {number} is {number ** 3}")
    