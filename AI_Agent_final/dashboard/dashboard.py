import streamlit as st
import pandas as pd

st.title("AI Agent Performance Dashboard")

data = pd.DataFrame({
    "Agent": ["DataAnalysisAgent"],
    "Tasks Completed": [10],
    "Accuracy (%)": [95],
    "Resource Utilization (%)": [70]
})

st.table(data)
st.bar_chart(data[["Accuracy (%)", "Resource Utilization (%)"]])
