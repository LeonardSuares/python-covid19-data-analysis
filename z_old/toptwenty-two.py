import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import sqlite3
import os
import plotly.express as px
from plotly.subplots import make_subplots
import  plotly.graph_objects as go

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
group_data = read_data(path, 'full_grouped.csv')


labels = world_data[0:15]['Country/Region'].values
cases = ['TotalCases', 'TotalDeaths', 'TotalRecovered', 'ActiveCases']
for i in cases:
    fig = px.pie(world_data[0:15], values=i, names=labels, hole=0.3, title='{} recorded w.r.t to WHO region countries'.format(i))
    fig.show()

world_data['Death_to_confirmed'] = world_data['TotalDeaths']/world_data['TotalCases']
world_data['Death_to_recovered'] = world_data['TotalDeaths']/world_data['TotalRecovered']
world_data['serious_to_deaths'] = world_data['Serious,Critical']/world_data['TotalDeaths']
world_data['Tests_to_confirmed'] = world_data['TotalTests']/world_data['TotalCases']

top_20_ratio = world_data.sort_values(by='Death_to_confirmed', ascending=False).head(20)

fig2 = px.bar(top_20_ratio, x='Country/Region', y='Death_to_confirmed', title= 'Deaths to confirmed ratio by countries')
fig2.show()

top_20_ratio = world_data.sort_values(by='Death_to_recovered', ascending=False).head(20)

fig3 = px.bar(top_20_ratio, x='Country/Region', y='Death_to_recovered', title= 'Deaths to Recovered ratio by countries')
fig3.show()

top_20_ratio = world_data.sort_values(by='serious_to_deaths', ascending=False).head(20)

fig4 = px.bar(top_20_ratio, x='Country/Region', y='serious_to_deaths', title= 'Serious to Deaths ratio by countries')
fig4.show()

top_20_ratio = world_data.sort_values(by='Tests_to_confirmed', ascending=False).head(20)

fig5 = px.bar(top_20_ratio, x='Country/Region', y='Tests_to_confirmed', title= 'Tests to Confirmed ratio by countries')
fig5.show()

print(group_data.head)


def country_visualization(df, country):
    data = df[df['Country/Region'] == country]
    data2 = data.loc[:, ['Date', 'Confirmed', 'Deaths', 'Recovered', 'Active']]

    fig = make_subplots(
        rows=1, cols=4,
        subplot_titles=('Confirmed', 'Active', 'Recovered', 'Deaths')
    )

    # Note: Use go.Scatter (Capital 'S'), not go.scatter
    fig.add_trace(
        go.Scatter(name='Confirmed', x=data2['Date'], y=data2['Confirmed']), row=1, col=1
    )
    fig.add_trace(
        go.Scatter(name='Deaths', x=data2['Date'], y=data2['Deaths']), row=1, col=2
    )
    fig.add_trace(
        go.Scatter(name='Recovered', x=data2['Date'], y=data2['Recovered']), row=1, col=3
    )
    fig.add_trace(
        go.Scatter(name='Active', x=data2['Date'], y=data2['Active']), row=1, col=4
    )

    fig.update_layout(
        height=600,
        width=1000,
        title_text='Date vs Recorded cases of {}'.format(country),
        template='plotly_dark'
    )
    fig.show()

country_visualization(group_data, 'Brazil')