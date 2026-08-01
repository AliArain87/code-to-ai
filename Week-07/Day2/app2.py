import streamlit as st
import pandas as pd
from datetime import time, datetime

st.title("My Web Dashboard")
st.header("This is my streamlit code")
st.write("Hello how are you?")

# data load
df = pd.read_csv("gapminder.csv")

st.dataframe(df.head())

opt = st.selectbox("Select any values",[1,2,3,4], index=0, help="You have to choose 1 to 4 number out of these available options",placeholder="Hey Ali")

if opt == 2:
    st.snow()
elif opt == 3:
    st.write("You got it with 3")
    st.balloons()



opt2 = st.slider("This is slider", min_value=0, max_value=100, value= 25, step=50)


age = st.slider("How old are you?", 0, 130, 25)
st.write("I'm ", age, "years old")

values = st.slider("Select a range of values", 0.0, 100.0, (25.0, 75.0))
st.write("Values:", values)

appointment = st.slider(
    "Schedule your appointment:", value=(time(11, 30), time(12, 45))
)
st.write("You're scheduled for:", appointment)


start_time = st.slider(
    "When do you start?",
    value=datetime(2020, 1, 1, 9, 30),
    format="MM/DD/YY - hh:mm",
)
st.write("Start time:", start_time)


d = st.date_input("When's your birthday")
st.write("Your birthday is:", d)