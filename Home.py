import streamlit as st
import plotly.express as px
from utils import load_all_data

st.set_page_config(page_title="Covid-19 Global Monitor", layout="wide", page_icon="🦠")

st.title("🦠 Covid-19 Global Intelligence Dashboard")
world_data, group_data, daywise_data = load_all_data()

# --- GLOBAL KPIs ---
st.subheader("Current Global Totals")
c1, c2, c3, c4 = st.columns(4)

c1.metric("Total Cases", f"{world_data['TotalCases'].sum():,.0f}")
c2.metric("Total Deaths", f"{world_data['TotalDeaths'].sum():,.0f}")
c3.metric("Total Recovered", f"{world_data['TotalRecovered'].sum():,.0f}")
c4.metric("Active Cases", f"{world_data['ActiveCases'].sum():,.0f}")

st.divider()

# --- GLOBAL TREND ---
st.subheader("Global Case Trend Over Time")
fig_trend = px.line(daywise_data, x='Date', y=['Confirmed', 'Deaths', 'Recovered', 'Active'],
                    title="Global Progression (Day-wise)", color_discrete_sequence=px.colors.qualitative.Set1)
st.plotly_chart(fig_trend, use_container_width=True)