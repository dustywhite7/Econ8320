# Import statements
import re
import requests
import pandas as pd
import numpy as np

# Import our plotting library
import plotly.express as px

# Grab and clean the data
url = "https://github.com/dustywhite7/Econ8320/raw/refs/heads/master/AssignmentData/world_bank_data_2023.csv"
data = pd.read_csv(url)
gdp = data.loc[data['Series Name']=="GDP per capita (current US$)"]
gdp['2023 [YR2023]'] = gdp['2023 [YR2023]'].replace("..", np.nan)
gdp['2023 [YR2023]'] = gdp['2023 [YR2023]'].astype(float)

# Subset the data to only look at two countries
plotData = gdp.loc[(gdp['Country Name']=="Finland")| (gdp['Country Name']=='Uruguay'), ['Country Name', '2023 [YR2023]']]

# Make the plot
px.bar(plotData,x = 'Country Name', y = '2023 [YR2023]', color='Country Name')

