from dash import html, dcc 
import dash_bootstrap_components as dbc

from fronted.Navegador.navegador import navegador
from fronted.Datos.datos import *

layout = dbc.Container(
        [
        dbc.Row(
            [
            dbc.Col(navegador, md = 12, style={'background-color':'#DEC9D6'}),
            dbc.Col(Informacion_general, md = 12, style={'background-color':'#DEC9D6'}),
            dbc.Col(Informacion_nodos, md = 6, style={'background-color':'#C9A7EB'}),
            dbc.Col(Informacion_elementos, md = 6, style={'background-color':'#B08BBB'}),
            dbc.Col(Apoyos, md = 6, style={'background-color':'#B08BBB'}),
            dbc.Col(Cargas_conocidas, md = 6, style={'background-color':'#C9A7EB'}),
            dbc.Col(Calculo_matriz_total, md = 12, style={'background-color':'#dfcae1'}),

             ]
            ),
            ]
                        )
