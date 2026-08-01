import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

st.title("My First Streamlit App")
st.write("Hello! This is a web page built with Python.")

df = pd.read_csv("gapminder.csv")
st.header("A peek at the data")
st.dataframe(df.head())


