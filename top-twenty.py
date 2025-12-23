import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import sqlite3
import os
import plotly.express as px


# 1. Shows all columns (You already have this)
pd.set_option('display.max_columns', None)

# 2. DISABLES WRAPPING by setting the display width to a very high number
pd.set_option('display.width', 1000)

import  warnings
from warnings import filterwarnings
filterwarnings("ignore")

files = os.listdir(r'C:\Users\leona\PycharmProjects\Python Data Analysis Projects\Covid19-data-analysis\Covid-19-20251222T220640Z-1-001\Covid-19')
print(files)

def read_data(path, filename):
    return pd.read_csv(path+'/'+filename)

path = r'C:\Users\leona\PycharmProjects\Python Data Analysis Projects\Covid19-data-analysis\Covid-19-20251222T220640Z-1-001\Covid-19'
world_data = read_data(path, 'worldometer_data.csv')
province_data = read_data(path, files[1])
daywise_data = read_data(path, files[2])
group_data = read_data(path, files[3])
full_group_data = read_data(path, files[4])
usa_data = read_data(path, files[5])
print(world_data.columns)

pop_test_ratio = world_data['Population']/world_data['TotalTests'].iloc[0:20]
# fig = px.bar(world_data.iloc[0:20], x='Country/Region', y=pop_test_ratio[0:20], color= 'Country/Region', title='Population to test done ratio')
# fig.show()
# print(pop_test_ratio)

fig3 = px.bar(world_data.iloc[0:20], x='Country/Region', y=['Serious,Critical','TotalDeaths','TotalRecovered','ActiveCases','TotalCases'])
fig3.show()