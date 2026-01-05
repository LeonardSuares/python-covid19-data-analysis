import streamlit as st
import plotly.express as px
from utils import load_all_data

st.set_page_config(page_title="Regional Analysis", layout="wide")
st.title("🗺️ Regional Impact & Recovery Analysis")
world_data, _, _ = load_all_data()

# --- Existing Treemap Section ---
st.subheader("Global Distribution")
metric = st.selectbox("Select Metric for Treemap",
                     ['TotalCases', 'TotalDeaths', 'TotalRecovered', 'ActiveCases'])

fig_tree = px.treemap(world_data.iloc[0:20], path=['Country/Region'], values=metric,
                     color=metric, color_continuous_scale='RdBu',
                     title=f"Treemap: {metric} by Country")
st.plotly_chart(fig_tree, use_container_width=True)

st.divider()

# --- NEW: REGIONAL COMPARISON (The Recovery Chart) ---
st.subheader("🌍 Regional Recovery Comparison")
st.write("Compare the recovery and mortality efficiency across different WHO Regions.")

# Add a prompt to switch between metrics
comparison_metric = st.radio(
    "Select Comparison View:",
    ["Recovery Rate (%)", "Mortality Rate (%)"],
    horizontal=True,
    help="Recovery Rate = (Recovered / Total Cases) * 100"
)

# Calculate Regional Stats
regional_stats = world_data.groupby('WHO Region').agg({
    'TotalCases': 'sum',
    'TotalDeaths': 'sum',
    'TotalRecovered': 'sum'
}).reset_index()

# Define the formulas
regional_stats['Recovery Rate (%)'] = (regional_stats['TotalRecovered'] / regional_stats['TotalCases']) * 100
regional_stats['Mortality Rate (%)'] = (regional_stats['TotalDeaths'] / regional_stats['TotalCases']) * 100

# Sort based on the selected metric
sorted_stats = regional_stats.sort_values(comparison_metric, ascending=False)

# Render Chart
fig_regional = px.bar(
    sorted_stats,
    x='WHO Region',
    y=comparison_metric,
    color=comparison_metric,
    color_continuous_scale='Greens' if "Recovery" in comparison_metric else 'Reds',
    text_auto='.1f',
    title=f"Regional {comparison_metric}"
)

fig_regional.update_layout(yaxis_title="Percentage (%)", showlegend=False)
st.plotly_chart(fig_regional, use_container_width=True)