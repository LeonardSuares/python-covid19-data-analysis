import streamlit as st
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from utils import load_all_data

st.title("🔎 Individual Country Deep Dive")
_, group_data, _ = load_all_data()

# Searchable dropdown for countries
all_countries = sorted(group_data['Country/Region'].unique())
country = st.selectbox("Search and Select a Country", all_countries, index=all_countries.index('Brazil'))

# Filtering data for selected country
data = group_data[group_data['Country/Region'] == country]

fig = make_subplots(rows=1, cols=4, subplot_titles=('Confirmed', 'Active', 'Recovered', 'Deaths'))

traces = [('Confirmed', 1), ('Active', 2), ('Recovered', 3), ('Deaths', 4)]
for name, col in traces:
    fig.add_trace(go.Scatter(name=name, x=data['Date'], y=data[name]), row=1, col=col)

fig.update_layout(height=500, title_text=f"Historical Progression: {country}", template='plotly_dark')
st.plotly_chart(fig, use_container_width=True)