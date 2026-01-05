import pandas as pd
import streamlit as st
import os


@st.cache_data
def load_all_data():
    # Relative paths for portability
    world = pd.read_csv(os.path.join("data", "worldometer_data.csv"))
    grouped = pd.read_csv(os.path.join("data", "full_grouped.csv"))
    daywise = pd.read_csv(os.path.join("data", "day_wise.csv"))

    # 1. Clean Dates
    grouped['Date'] = pd.to_datetime(grouped['Date'])
    daywise['Date'] = pd.to_datetime(daywise['Date'])

    # 2. Add Ratio Columns to World Data (Centralized logic)
    world['Death_to_confirmed'] = (world['TotalDeaths'] / world['TotalCases']) * 100
    world['Death_to_recovered'] = (world['TotalDeaths'] / world['TotalRecovered']) * 100
    world['Tests_to_confirmed'] = (world['TotalTests'] / world['TotalCases']) * 100

    return world, grouped, daywise