# Importing modules
import pandas as pd 
import seaborn as sns
import matplotlib.pyplot as plt 
import streamlit as st


# Basic structure of streamlit web app

sns.set_theme(style='whitegrid')

st.title("Gapminder Explorer💡")
st.write(
    "Explore how life expectancy, income, and population changed around the "
    "world from 1952 to 2007. Use the controls on the left to filter the data."
)


# Importing the data from csv
df = pd.read_csv('gapminder.csv')


st.sidebar.header("Options for users")

# sidebar - selectbox for continent
continent = sorted(df['continent'].unique())
chosen_continents = st.sidebar.selectbox("Choose the Continent", continent)


# siderbar - slider for year
year = sorted(df['year'].unique())
chosen_year = st.sidebar.slider("Choose an year", int(min(year)), max_value=int(max(year)), step=5, value=2007)

# filtering data

filtered_data = df[(df['continent'] == chosen_continents) & (df['year']== chosen_year)]

st.header(f"{chosen_continents} in {chosen_year}")
st.warning(f"Showing {len(filtered_data)} countries.")
st.dataframe(filtered_data)

# ---------- Chart 1: trend over time for the chosen continent ----------
st.subheader("Average life expectancy over time")
trend = df[df["continent"] == chosen_continents].groupby("year")["lifeExp"].mean()

fig1, ax1 = plt.subplots(figsize=(8, 4))
ax1.plot(trend.index, trend.values, marker="o", color="teal")
ax1.set_title(f"Average Life Expectancy in {chosen_continents} (1952-2007)")
ax1.set_xlabel("Year")
ax1.set_ylabel("Life Expectancy (years)")
st.pyplot(fig1)


# ---------- Chart 2: comparison bar for the chosen year ----------
st.subheader("Continents compared in the chosen year")
year_data = df[df["year"] == chosen_year]

fig2, ax2 = plt.subplots(figsize=(8, 4))
sns.barplot(data=year_data, x="continent", y="lifeExp", ax=ax2, hue='continent')
ax2.set_title(f"Average Life Expectancy by Continent ({chosen_year})")
ax2.set_xlabel("Continent")
ax2.set_ylabel("Life Expectancy (years)")
st.pyplot(fig2)


# ---------- Chart 3: relationship scatter for the chosen year ----------
st.subheader("Income vs life expectancy in the chosen year")
fig3, ax3 = plt.subplots(figsize=(8, 5))
sns.scatterplot(data=year_data, x="gdpPercap", y="lifeExp",
                hue="continent", alpha=0.7, ax=ax3)
ax3.set_title(f"Income vs Life Expectancy ({chosen_year})")
ax3.set_xlabel("GDP per person")
ax3.set_ylabel("Life Expectancy (years)")
st.pyplot(fig3)