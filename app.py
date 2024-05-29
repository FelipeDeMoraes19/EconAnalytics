from dash import Dash, dcc, html
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd
import os

def load_cleaned_data(filename):
    filepath = os.path.join('data/processed', filename)
    if os.path.exists(filepath):
        data = pd.read_csv(filepath)
        return data
    else:
        raise FileNotFoundError(f"File {filepath} does not exist.")

gdp_data = load_cleaned_data('gdp_data_cleaned.csv')
print(gdp_data.head())  
inflation_data = load_cleaned_data('inflation_data_cleaned.csv')
print(inflation_data.head())  
unemployment_data = load_cleaned_data('unemployment_data_cleaned.csv')
print(unemployment_data.head())  

app = Dash(__name__)

app.layout = html.Div(children=[
    html.H1(children='Economic Indicators Dashboard'),

    dcc.Tabs([
        dcc.Tab(label='GDP', children=[
            dcc.Graph(
                id='gdp-graph',
                figure=px.line(gdp_data, x='date', y='value', title='GDP Over Time')
            )
        ]),
        dcc.Tab(label='Inflation', children=[
            dcc.Graph(
                id='inflation-graph',
                figure=px.line(inflation_data, x='date', y='value', title='Inflation Over Time')
            )
        ]),
        dcc.Tab(label='Unemployment', children=[
            dcc.Graph(
                id='unemployment-graph',
                figure=px.line(unemployment_data, x='date', y='value', title='Unemployment Rate Over Time')
            )
        ])
    ])
])

if __name__ == '__main__':
    app.run_server(debug=True)
