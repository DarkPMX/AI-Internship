import streamlit as st

st.title("🎮 My Fun App")

name = st.text_input("What's your name?")
mood = st.selectbox("How are you feeling today?", ["Happy 😀", "Sad 😞", "Excited 😁", "Bored 😐"])

if "visits" not in st.session_state:
    st.session_state.visits = 0

if st.button("Say Hello!"):
    st.session_state.visits += 1
    st.write(f"Hello, {name}! You are feeling {mood}.")
    st.write(f"You have visited this app {st.session_state.visits} times.")

st.image("https://media.giphy.com/media/3o7abKhOpu0NwenH3O/giphy.gif", caption="Enjoy your day!")   