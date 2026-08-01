import streamlit as st
import seaborn as sns
import pandas as pd
import plotly.express as px


st.set_page_config(
    page_title="Restaurant Dashboard",
    page_icon="📊",
    layout="wide"
)


st.title("📊 Restaurant Tips Dashboard")

st.write("Analyze restaurant tips using the Seaborn Tips dataset.")


tips = sns.load_dataset("tips")

st.sidebar.header("Filters")

sex = st.sidebar.multiselect(
    "Gender",
    tips["sex"].unique(),
    default=tips["sex"].unique()
)

day = st.sidebar.multiselect(
    "Day",
    tips["day"].unique(),
    default=tips["day"].unique()
)

time = st.sidebar.multiselect(
    "Time",
    tips["time"].unique(),
    default=tips["time"].unique()
)

smoker = st.sidebar.multiselect(
    "Smoker",
    tips["smoker"].unique(),
    default=tips["smoker"].unique()
)


filtered = tips[
    (tips["sex"].isin(sex)) &
    (tips["day"].isin(day)) &
    (tips["time"].isin(time)) &
    (tips["smoker"].isin(smoker))
]


col1, col2, col3, col4 = st.columns(4)

col1.metric("Total Bills", f"${filtered['total_bill'].sum():.2f}")

col2.metric("Total Tips", f"${filtered['tip'].sum():.2f}")

col3.metric("Average Tip", f"${filtered['tip'].mean():.2f}")

col4.metric("Customers", len(filtered))


fig = px.histogram(
    filtered,
    x="total_bill",
    nbins=20,
    title="Distribution of Total Bills"
)

st.plotly_chart(fig, use_container_width=True)


fig = px.scatter(
    filtered,
    x="total_bill",
    y="tip",
    color="day",
    size="size",
    hover_data=["sex"],
    title="Bill vs Tip"
)

st.plotly_chart(fig, use_container_width=True)


day_tip = filtered.groupby("day")["tip"].mean().reset_index()

fig = px.bar(
    day_tip,
    x="day",
    y="tip",
    color="day",
    title="Average Tip by Day"
)

st.plotly_chart(fig, use_container_width=True)



fig = px.pie(
    filtered,
    names="sex",
    title="Customers by Gender"
)

st.plotly_chart(fig, use_container_width=True)



fig = px.box(
    filtered,
    x="day",
    y="tip",
    color="day",
    title="Tip Distribution by Day"
)

st.plotly_chart(fig, use_container_width=True)



corr = filtered[["total_bill", "tip", "size"]].corr()

fig = px.imshow(
    corr,
    text_auto=True,
    color_continuous_scale="Blues",
    title="Correlation Heatmap"
)

st.plotly_chart(fig, use_container_width=True)



st.subheader("Filtered Data")

st.dataframe(filtered, use_container_width=True)


csv = filtered.to_csv(index=False)

st.download_button(
    "Download CSV",
    csv,
    "tips.csv",
    "text/csv"
)


