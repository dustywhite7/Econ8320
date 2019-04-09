import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import plotly.graph_objs as go
from dash.dependencies import Input, Output

df = pd.read_csv(
    'https://raw.githubusercontent.com/plotly/'
    'datasets/master/gapminderDataFiveYear.csv')

app = dash.Dash()

app.layout = html.Div([
            html.H1("GDP Per Capita and Life Expectancy"), # OR
#            dcc.Markdown("# GDP Per Capita and Life Expectancy"),
            dcc.Dropdown(
                id='continents',
                options=[{'label': i, 'value': i} for i in list(df.continent.unique()) + ['All']],
                value='All'
            ),
            dcc.RadioItems(
                    id='xaxis-type',
                    options=[{'label': i, 'value': i} for i in ['Linear', 'Log']],
                    value='Log',
                    labelStyle={'display': 'inline-block'}
                ),    
            dcc.Graph(id='graph-with-slider'),
            dcc.Slider(
                id='year-slider',
                min=df['year'].min(),
                max=df['year'].max(),
                value=df['year'].min(),
                step=None,
                marks={str(year): str(year) for year in df['year'].unique()}
            )
            
        ],
        style={'width': '48%', 'display': 'inline-block'})


@app.callback(
    Output('graph-with-slider', 'figure'),
    [Input('year-slider', 'value'),
     Input('xaxis-type','value'),
     Input('continents','value')])

def update_figure(selected_year, axis_type, continent):
    if continent=="All":
        filtered_df = df
    else:
        filtered_df = df[df['continent']==continent]
    filtered_df = filtered_df[filtered_df.year == selected_year]
    traces = []
    for i in filtered_df.continent.unique():
        df_by_continent = filtered_df[filtered_df['continent'] == i]
        traces.append(go.Scatter(
            x=df_by_continent['gdpPercap'],
            y=df_by_continent['lifeExp'],
            text=df_by_continent['country'],
            mode='markers',
            opacity=0.7,
            marker={
                'size': 15,
                'line': {'width': 0.5, 'color': 'white'}
            },
            name=i
        ))

    return {
        'data': traces,
        'layout': go.Layout(
            xaxis={'type': 'linear' if axis_type == 'Linear' else 'log',
                   'title': 'GDP Per Capita'},
            yaxis={'title': 'Life Expectancy', 'range': [20, 90]},
            margin={'l': 40, 'b': 40, 't': 10, 'r': 10},
            legend={'x': 0, 'y': 1},
            hovermode='closest'
        )
    }


if __name__ == '__main__':
    app.run_server(port=80, host='0.0.0.0')
