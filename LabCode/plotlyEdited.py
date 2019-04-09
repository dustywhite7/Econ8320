#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 11 10:45:11 2018

@author: dusty
"""

from plotly.offline import plot
import plotly.graph_objs as go
import numpy as np

trace = go.Scatter( # initialize scatter object
  x = list(range(2000,2010)), # pass x, y values
  y = [29.8,30.1,30.5,30.6,31.3,31.7,32.6,33.1,32.7,32.8])

plotdata=go.Data([trace]) # Process the plots

plot(plotdata) # Render the plots

#%%

trace = go.Scatter( # initialize scatter object
  x = list(range(2000,2010)), # pass x, y values
  y = [29.8,30.1,30.5,30.6,31.3,31.7,32.6,33.1,32.7,32.8],
  marker =  {'color': 'green', # choose the marker color
    'symbol': 0, # choose a shape
    'size': 20}, # choose a size
    ) 

plotdata=go.Data([trace]) # Process the plots

plot(plotdata) # Render the plots

#%%

trace = go.Scatter( # initialize scatter object
  x = list(range(2000,2010)), # pass x, y values
  y = [29.8,30.1,30.5,30.6,31.3,31.7,32.6,33.1,32.7,32.8],
  marker =  {'color': 'green', # choose the marker color
    'symbol': 0, # choose a shape
    'size': 20}, # choose a size
    line=dict(
        shape='spline' # spline smoothing
    )) 

plotdata=go.Data([trace]) # Process the plots

plot(plotdata) # Render the plots

#%%

trace = go.Scatter( # initialize scatter object
  x = list(range(2000,2010)), # pass x, y values
  y = [29.8,30.1,30.5,30.6,31.3,31.7,32.6,33.1,32.7,32.8],
  marker =  {'color': 'green', # choose the marker color
    'symbol': 0, # choose a shape
    'size': 20}, # choose a size
    line=dict(
        shape='spline' # spline smoothing
    ),
    text=['Year: ' + str(i) for i in list(range(2000,2010))], # hover text
    name='PCC') # name for legends

plotdata=go.Data([trace]) # Process the plots

plot(plotdata) # Render the plots


#%%

trace = go.Scatter( # initialize scatter object
  x = list(range(2000,2010)), # pass x, y values
  y = [29.8,30.1,30.5,30.6,31.3,31.7,32.6,33.1,32.7,32.8],
  marker =  {'color': 'green', # choose the marker color
    'symbol': 0, # choose a shape
    'size': 20}, # choose a size
    line=dict(
        shape='spline' # spline smoothing
    ),
    text=['Year: ' + str(i) for i in list(range(2000,2010))], # hover text
    name='PCC') # name for legends
    
trace2 = go.Scatter( # initialize scatter object
  x = list(range(2000,2010)), # pass x, y values
  y = [327,456,509,497,596,573,661,741,809,717],
  marker =  {'color': 'grey', # choose the marker color
    'symbol': 0, # choose a shape
    'size': 20}, # choose a size
    line=dict(
        shape='spline' # spline smoothing
    ),
    text=['Year: ' + str(i) for i in list(range(2000,2010))], # hover text
    name='DIB',
    yaxis='y2') # name for legends

plotdata=go.Data([trace, trace2]) # Process the plots

layout=go.Layout(title="Cheese Consumption and Bedsheet Tragedies", 
                 # configure the plot
  xaxis={'title':'Year',
         'showgrid':False},  # layout and name
  yaxis={'title':'Pounds of Cheese',
         'showgrid':False},
  yaxis2={'title':"Deaths due to Becoming Tangled in Bedsheets",
          'overlaying': 'y',
          'side':'right',
          'showgrid':False})  # the axes.

figure=go.Figure(data=plotdata,layout=layout)
# combine data and layout code

plot(figure) # Render the plots

#%%

from sqlalchemy import create_engine
import pandas as pd

SELECT = """SELECT AVG(hhincome) AS hhincome, year 
  FROM ACS
  WHERE statefip=31 
  GROUP BY year
  ORDER BY year"""
conn = create_engine(
  'mysql+mysqlconnector://viewer:@dadata.cba.edu:3306/ACS'
  )

data = pd.read_sql(SELECT, conn)

trace = go.Scatter( # initialize scatter object
  x = data['year'], 
  y = data['hhincome'], 
  marker =  {'color': 'green', 
    'symbol': 0, 
    'size': 12},
  mode="markers+lines", 
  name='Household Income Over Time') 

plotdata=go.Data([trace]) 
layout=go.Layout(title="Household Income",
  xaxis={'title':'Year'},  
  yaxis={'title':'Income ($)'})  

figure=go.Figure(data=plotdata,layout=layout)
plot(figure)


#%%

SELECT = """SELECT AVG(hhincome) AS hhincome, year,
    statefip
  FROM ACS
  WHERE statefip=31 or statefip=19
  GROUP BY year, statefip
  ORDER BY year, statefip"""
conn = create_engine(
  'mysql+mysqlconnector://viewer:@dadata.cba.edu:3306/ACS'
  )

data = pd.read_sql(SELECT, conn)

traces = []
for i in data['statefip'].unique():
  small_data = data.loc[data['statefip']==i, :]
  traces.append(go.Scatter( # initialize scatter object
    x = small_data['year'], 
    y = small_data['hhincome'], 
    mode="markers+lines", 
    name='Household Income in {}'.format(i)))

plotdata=go.Data(traces) 
layout=go.Layout(title="Household Income",
  xaxis={'title':'Year'},  
  yaxis={'title':'Income ($)'})  

figure=go.Figure(data=plotdata,layout=layout)
plot(figure)

#%%

trace1 = go.Box(
  y=np.random.rand(100),
  name='Mean & SD',
  marker=dict(
    color='rgb(10, 140, 208)',
  ),
  boxmean='sd' # Shows quartiles AND Std Dev on plot
)

plotdata = go.Data([trace1])
figure = go.Figure(data=plotdata)
plot(figure)

#%%


trace1 = go.Histogram(
  x=np.random.randn(5000),
  histnorm='density',
  xbins=dict( # Declare bin size
    start=-4.0,
    end=4.0,
    size=0.1
  ),
  marker=dict( # Customize markers
    color='#FFD7E9',
  ),
  opacity=0.9
)

plotdata = go.Data([trace1])
figure = go.Figure(data=plotdata)
plot(figure)


#%%

import plotly.figure_factory as ff

x = np.random.randn(5000)  
hist_data = [x]
group_labels = ['Sample'] # Labels our 'rug' plot

fig = ff.create_distplot(hist_data, 
  group_labels, 
  bin_size=0.05,
  show_hist=True,  # Toggle histogram
  show_curve=True, # Toggle smoothed distribution
  show_rug=True    # Toggle rug plot
  )
  
plot(fig)


#%%

# Create an array of data (its from MNIST)
x = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,116,125,171,255,255,150,93,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,169,253,253,253,253,253,253,218,30,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,169,253,253,253,213,142,176,253,253,122,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,52,250,253,210,32,12,0,6,206,253,140,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,77,251,210,25,0,0,0,122,248,253,65,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,31,18,0,0,0,0,209,253,253,65,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,117,247,253,198,10,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,76,247,253,231,63,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,128,253,253,144,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,176,246,253,159,12,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,25,234,253,233,35,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,198,253,253,141,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,78,248,253,189,12,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,19,200,253,253,141,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,134,253,253,173,12,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,248,253,253,25,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,248,253,253,43,20,20,20,20,5,0,5,20,20,37,150,150,150,147,10,0,0,0,0,0,0,0,0,0,248,253,253,253,253,253,253,253,168,143,166,253,253,253,253,253,253,253,123,0,0,0,0,0,0,0,0,0,174,253,253,253,253,253,253,253,253,253,253,253,249,247,247,169,117,117,57,0,0,0,0,0,0,0,0,0,0,118,123,123,123,166,253,253,253,155,123,123,41,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
x = - np.array(x).reshape(28,28)


trace = go.Heatmap(z = x, colorscale = "Greys")
plotdata=[trace]
plot(plotdata)

#%%

data = pd.read_csv("corruption2018.csv")

plotdata = go.Choropleth(
        locations = data['Abbr'],
        z = data['Index'],
        text = (data['Name'], data['Index']),
        autocolorscale = False,
        colorscale = 'Picnic',
        showscale = True,
    )


figure = go.Figure(data=[plotdata])
plot(figure)

#%%

layout = go.Layout(
    title = "Percieved Corruption",
    geo = dict(projection = dict(type='orthographic'),
               showcoastlines=False,
               showcountries = False,
               showframe = False,
               showrivers=False,
               scope = 'world'
        )
    )

figure = go.Figure(data=[plotdata], layout=layout)
plot(figure)


#%%

data = pd.read_csv("displaced2018.csv")

plotdata = go.Scattergeo(
            locationmode = 'country names',
            locations = data['Name'],
            marker = dict(
                size = data['Displaced']/100000,
                line = dict(width = 0)
            ),
            text = data['Displaced']
            )

figure = go.Figure(data=[plotdata])
plot(figure)

#%%

data = pd.read_csv("/home/dusty/Econ8320/LabCode/displaced2018.csv")

plotdata = go.Scattergeo(
            locationmode = 'country names',
            locations = data['Name'],
            marker = dict(
                size = data['Displaced']/100000,
                line = dict(width = 0)
            ),
            text = data['Displaced']
            )

layout = go.Layout(
    title = "Percieved Corruption",
    geo = dict(projection = dict(type='orthographic'),
               showcountries = True,
        )
    )

figure = go.Figure(data=[plotdata], layout=layout)
plot(figure)