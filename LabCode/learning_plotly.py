# Import statements
import re
import requests
import pandas as pd

# Import our plotting library
import plotly.express as px

# Grab and clean the data
url = "https://www.cia.gov/library/publications/the-world-factbook/rankorder/rawdata_2004.txt"
data = requests.get(url).text.replace("\r","").split("\n")
data = pd.DataFrame([re.split(r'[ ]{2,100}', i)[:3] for i in data], columns = ['rank', 'country', "GDP_per_capita"]).dropna()

# Subset the data to only look at two countries
plotData = data.loc[(data['country']=="Finland")| (data['country']=='Uruguay'), ['country', 'GDP_per_capita']]

# Make the plot
px.bar(plotData,x = 'country', y = 'GDP_per_capita', color='country')