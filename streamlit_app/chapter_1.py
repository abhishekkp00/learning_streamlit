import streamlit as st

st.title("Hello, Abhishek!")
st.subheader("Welcome to your Streamlit app.")
st.text("This is a simple example to get you started with Streamlit.")
st.write("Choose ypur fav. color:")

colors= st.selectbox("Pick a color", ["Red", "Green", "Blue", "Yellow"])
st.write(f"You selected: {colors}")
 

st.success("Your color is added successfully!")