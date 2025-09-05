#layouts in stremlit
import streamlit as st

st.title("Chai Taste Poll")

col1, col2 = st.columns(2)
with col1:
    st.header("Masala Chai")
    st.image("https://images.pexels.com/photos/3904035/pexels-photo-3904035.jpeg", width=200)
    vote1 = st.button("Vote for Masala Chai")

with col2:
    st.header("Ginger Chai")
    st.image("https://images.pexels.com/photos/5946616/pexels-photo-5946616.jpeg", width=200)
    vote2 = st.button("Vote for Ginger Chai")

if vote1:
    st.success("You voted for Masala Chai!")
if vote2:
    st.success("You voted for Ginger Chai!")

name= st.sidebar.text_input("Enter your name")
tea= st.sidebar.selectbox("Choose your favorite tea", ["Masala Chai", "Ginger Chai", "Green Tea", "Black Tea"]) #goes to sidebar

st.write(f"Welcome, {name}! You selected {tea} as your favorite tea.") #goes to main page

with st.expander("See Tea Facts"):
    st.write("""
    - Tea is the second most consumed beverage in the world after water.
    - There are many types of tea including black, green, white, oolong, and herbal.
    - Tea contains antioxidants which can help improve health.
    - The tradition of tea drinking dates back thousands of years.
    """)

st.markdown("### WELCOME TO THE TEA POLL APP" ) #markdown for header
st.markdown('>This is a simple app to vote for your favorite type of tea. Enjoy your tea time!') #block quote