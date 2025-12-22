import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import sqlite3
import os

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
usa_data = read_data(path, files[4])