import streamlit as st
import pandas as pd
import plotly.express as px

# Loading data from csv using pandas and Extracting only required columns
df = pd.read_csv("happy.csv")[["happiness", "gdp", "generosity"]]

st.title("Where's the happiness")
feed_list= [x.title() for x in df.columns]
option_1 = st.selectbox("Select the data for X-axis", feed_list)
option_2 = st.selectbox("Select the data for Y-axis", feed_list)

st.subheader(f"{option_1} and {option_2}")

figure = px.scatter(x=df[option_1.lower()], y=df[option_2.lower()], labels={"x": option_1, "y": option_2})

st.plotly_chart(figure)

