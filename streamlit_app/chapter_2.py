import streamlit as st

st.title("Chai Maker App")
if st.button("Make Chai"):
    st.success("Chai is being prepared!")
    
masala=st.checkbox("Add Masala")
if masala:
    st.write("Masala added!")

tea_type=st.radio("Select Tea Type", ["Black Tea", "Green Tea", "Herbal Tea"])
st.write(f"You selected: {tea_type}")

flavour=st.selectbox("Choose a flavour", ["Cardamom", "Ginger", "Saffron", "Mint"])
st.write(f"You selected: {flavour}")
st.success("Your flavour is added successfully!")

sugar=st.slider("Select sugar level (in tsp)", 0, 5, 2) # default is 2, from 0 to 5
st.write(f"Selected sugar level is: {sugar}")

#for uncontrolled input

cups= st.number_input("Enter number of cups", min_value=1, max_value=10, value=1, step=1)
st.write(f"You want {cups} cup(s) of chai.")

name= st.text_input("Enter your name")
if name:
    st.write(f"Hello, {name}! Your chai will be ready soon.")

dob = st.date_input("Enter your date of birth")
st.write(f"Your date of birth is: {dob}")
st.success("Your color is added successfully!")