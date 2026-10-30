import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Enterprise Project Tracker", layout="wide")
st.title("📊 Enterprise Project Management & Risk Dashboard")

# Enterprise Project Dataset
data = {
    "Project": ["AI Sales Assistant", "CPG Trade Promo", "SaaS Migration", "Inventory Engine"],
    "Allocated Budget ($)": [120000, 85000, 150000, 95000],
    "Actual Spend ($)": [135000, 80000, 142000, 110000],
    "Delayed Tasks": [5, 1, 2, 7],
    "Risk Level": ["High", "Low", "Medium", "Critical"]
}

df = pd.DataFrame(data)
df["Variance ($)"] = df["Actual Spend ($)"] - df["Allocated Budget ($)"]

# Top Metrics Row
c1, c2, c3 = st.columns(3)
c1.metric("Active Enterprise Projects", len(df))
c2.metric("Total Budget Allocated", f"${df['Allocated Budget ($)'].sum():,}")
c3.metric("Total Net Variance", f"${df['Variance ($)'].sum():,}")

st.markdown("---")

# Visual Charts
col_left, col_right = st.columns(2)

with col_left:
    st.subheader("Allocated Budget vs Actual Spend")
    fig1 = px.bar(df, x="Project", y=["Allocated Budget ($)", "Actual Spend ($)"], barmode="group")
    st.plotly_chart(fig1, use_container_width=True)

with col_right:
    st.subheader("Delayed Tasks Distribution")
    fig2 = px.pie(df, names="Project", values="Delayed Tasks", color="Risk Level")
    st.plotly_chart(fig2, use_container_width=True)

st.subheader("Project Execution Summary")
st.dataframe(df)