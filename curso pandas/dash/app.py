import dash
from dash import html, dcc, Input, Output
import pandas as pd
import plotly.express as px
import numpy as np

df_ = pd.read_csv('curso pandas/dados_final.csv')

app = dash.Dash(__name__)

app.layout = html.Div([
    html.H1('Dashboard de desocupação'),
    html.H3('Valores por sexo'),
    
    dcc.Graph(id = 'graph_sex'),
    dcc.Dropdown(
        id = 'dropdown_indicator',
        options = {'Taxa de desocupação':'Taxa de desocupação',
                   'Nível da ocupação':'Nível da ocupação',
                   'Participação':'Nível de participação',
                   'Renda habitual total':'Renda habitual total',
                   'Renda habitual principal':'Renda habitual principal',
                   'Renda efetiva total':'Renda efetiva total',
                   'Renda efetiva principal':'Renda efetiva principal'},
        value = 'Taxa de desocupação'
    ),
    dcc.Dropdown(
        id = 'dropdown_period',
        options = {"1° Tri.":"1° Tri.",
                   "2° Tri.":"2° Tri.",
                   "3° Tri.":"3° Tri.",
                   "4° Tri.":"4° Tri.",
                   "Tri.":"Todos"},
        value = "Tri."
    ),
    dcc.Dropdown(
        id = 'dropdown_region',
        options = {"Brasil":"Brasil",
                  "Nordeste":"Nordeste",
                  "Ceará":"Ceará",
                  "Todos":"Todos"},
        value = "Brasil"
    ),
    dcc.Dropdown(
        id = 'dropdown_sex',
        options = {"Mulher":"Mulher",
                   "Homem":"Homem",
                   "nan":"Geral"},
        value = "nan"
    )
])

@app.callback(
    Output('graph_sex', 'figure'),
    [Input('dropdown_indicator', 'value'),
     Input('dropdown_period', 'value'),
     Input('dropdown_region', 'value'),
     Input('dropdown_sex', 'value')]
)
def uptade_figure(selected_indicator, selected_period, selected_region, selected_sex):
    df_copia = df_.copy()

    if selected_indicator:
        df_copia = df_copia[['Fonte', 'Sexo', 'Local', selected_indicator]]

    if selected_period:
        df_copia = df_copia[df_copia['Fonte'].str.contains(selected_period)]
    
    if selected_region != "Todos":
        df_copia = df_copia[df_copia['Local'] == selected_region]
    
    if selected_sex != "nan":
        df_copia = df_copia[df_copia['Sexo'] == selected_sex]
    else:
        df_copia = df_copia[df_copia['Sexo'].isna()]
        
        
    fig = px.line(
        df_copia,
        x = 'Fonte', y = selected_indicator,
        color = 'Local',
        labels = {'Fonte': 'Período',
                  selected_indicator:selected_indicator,
                  'Local':'Região Geográfica'}
    )

    return fig

if __name__ == '__main__':
    app.run(debug = True)