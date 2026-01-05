import streamlit as st
import plotly.express as px
from utils import load_all_data

st.title("📊 Critical Ratio Rankings")
world_data, _, _ = load_all_data()

# Ratio Selector
ratio_choice = st.selectbox("Select Ratio to Rank",
                           ['Death_to_confirmed', 'Death_to_recovered', 'Tests_to_confirmed'])

st.subheader(f"Top 20 Countries by {ratio_choice.replace('_', ' ').title()}")

# Dynamic Sorting based on choice
top_20 = world_data.sort_values(by=ratio_choice, ascending=False).head(20)

fig_bar = px.bar(top_20, x='Country/Region', y=ratio_choice,
                 color=ratio_choice, color_continuous_scale='OrRd')
st.plotly_chart(fig_bar, use_container_width=True)