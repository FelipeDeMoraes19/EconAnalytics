import dash
from dash import dcc, html
import plotly.express as px
import pandas as pd
import os

app = dash.Dash(__name__)

# Função para carregar dados processados
def load_cleaned_data(filename):
    filepath = os.path.join('data', 'processed', filename)
    if os.path.exists(filepath):
        data = pd.read_csv(filepath)
        data['date'] = pd.to_datetime(data['date'])  # Convertendo 'date' para datetime
        return data
    else:
        print(f"File {filepath} does not exist.")
        return pd.DataFrame()

# Carregando dados
gdp_data = load_cleaned_data('gdp_data_cleaned.csv')
inflation_data = load_cleaned_data('inflation_data_cleaned.csv')
unemployment_data = load_cleaned_data('unemployment_data_cleaned.csv')

# Verificando os dados carregados
print("GDP Data:")
print(gdp_data.head())
print("Inflation Data:")
print(inflation_data.head())
print("Unemployment Data:")
print(unemployment_data.head())

app.layout = html.Div([
    html.H1("Economic Indicators Dashboard"),
    dcc.Tabs(id="tabs", children=[
        dcc.Tab(label='GDP', children=[
            html.Div([
                html.H2("GDP Over Time"),
                dcc.Graph(
                    id='gdp-graph',
                    figure=px.line(gdp_data, x='date', y='value', title='GDP Over Time')
                )
            ])
        ]),
        dcc.Tab(label='Inflation', children=[
            html.Div([
                html.H2("Inflation Over Time"),
                dcc.Graph(
                    id='inflation-graph',
                    figure=px.line(inflation_data, x='date', y='value', title='Inflation Over Time')
                )
            ])
        ]),
        dcc.Tab(label='Unemployment', children=[
            html.Div([
                html.H2("Unemployment Rate Over Time"),
                dcc.Graph(
                    id='unemployment-graph',
                    figure=px.line(unemployment_data, x='date', y='value', title='Unemployment Rate Over Time')
                )
            ])
        ])
    ])
])

if __name__ == '__main__':
    app.run_server(debug=True)
