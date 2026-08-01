
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


st.title("Gapminder Charts")

df = pd.read_csv("gapminder.csv")
df_2007 = df[df["year"] == 2007]

st.header("Life expectancy by continent (2007)")

# Build a figure and axes, draw on the axes, hand the figure to Streamlit
fig, ax = plt.subplots(figsize=(8, 5))
sns.barplot(data=df_2007, x="continent", y="lifeExp", ax=ax)
ax.set_title("Average Life Expectancy by Continent (2007)")
ax.set_xlabel("Continent")
ax.set_ylabel("Life Expectancy (years)")

st.pyplot(fig)


st.button("Reset", type="primary")
if st.button("Say hello"):
    st.write("Why hello there")
else:
    st.write("Goodbye")

if st.button("Aloha", type="tertiary"):
    st.write("Ciao")

