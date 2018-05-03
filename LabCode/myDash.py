import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import plotly.graph_objs as go
from dash.dependencies import Input, Output
import numpy as np

"""
The data for this project comes from movielens, via grouplens.org
"""

df = pd.read_csv("movieData.csv",delimiter="\t")
df['year'] = pd.to_datetime(df['release']).dt.year
df.columns = [i.lower() for i in df.columns]

genres = ['Action', 'Adventure', 'Animation', 'Children',
       'Comedy', 'Crime', 'Documentary', 'Drama', 'Fantasy', 'FilmNoir',
       'Horror', 'Musical', 'Mystery', 'Romance', 'Scifi', 'Thriller', 'War',
       'Western']

app = dash.Dash()

app.layout = html.Div([
    html.H1("Movie Ratings"),
    html.H4("Choose a Year:"),
    dcc.Dropdown(
        id='year',
        options=[{'label': i, 'value': i} for i in ['All'] + sorted(list(df.year.unique()))[:-1]],
        value='All'
    ),
    html.H4("Choose a Genre:"),
    dcc.Dropdown(
        id='genre',
        options=[{'label': i, 'value': i} for i in ['All'] + sorted(genres)],
        value='All'
    ),  
    dcc.Graph(id='movieratings')
        
    ],
    style={'width': '48%', 'display': 'inline-block'})


@app.callback(Output('movieratings','figure'),
              [Input('year','value'),
               Input('genre','value')])

def update_figure(year, genre):
  if year=='All':
    small_df = df
  else:
    small_df = df[df['year']==year]
  if genre!='All':
    small_df = small_df[small_df[genre.lower()]==1]
  traces = []
  for x in sorted(small_df.occupation.unique()):
    y = np.mean(small_df.loc[small_df['occupation']==x, 'starsrating'])
    traces.append(go.Bar(
        x=[x.title()],
        y=[y],
        name=x.title()
        ))

  return {
    'data': traces,
    'layout': go.Layout(
      xaxis={'title': 'Occupation'},
      yaxis={'title': 'Star Rating', 'range':[np.min([traces[x].y[0] for x in range(len(traces))])-.2,np.max([traces[x].y[0] for x in range(len(traces))])+.2]},
      margin={'l': 40, 'b': 80, 't': 10, 'r': 10},
      showlegend=False,
      hovermode='closest'
    )
    }




if __name__ == '__main__':
    app.run_server()
    
