import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import streamlit as st

st.set_page_config(page_title="Chocolate Dashboard", layout="centered")
st.title("🍫 Chocolate Demand Dashboard")

# Load your dataset (Make sure the CSV name matches your uploaded file)
df = pd.read_csv("Chocolate_Sales.csv")

# Sidebar Filters
st.sidebar.header("🕹️ Control Panel")
selected_country = st.sidebar.multiselect(
    "Select Country:", options=df["Country"].unique(), default=df["Country"].unique()
)
selected_channel = st.sidebar.multiselect(
    "Select Channel:", options=df["Channel"].unique(), default=df["Channel"].unique()
)

filtered_df = df[
    (df["Country"].isin(selected_country))
    & (df["Channel"].isin(selected_channel))
]

# Simple Seaborn Plot
st.subheader("📦 Shipments by Sales Channel")
if not filtered_df.empty:
    sns.set_theme(style="darkgrid")
    fig, ax = plt.subplots(figsize=(6, 3.5))
    sns.barplot(
        data=filtered_df,
        x="Channel",
        y="Boxes_Shipped",
        estimator="sum",
        errorbar=None,
        ax=ax,
        palette="viridis",
    )
    st.pyplot(fig)
else:
    st.warning("No data selected!")
  
