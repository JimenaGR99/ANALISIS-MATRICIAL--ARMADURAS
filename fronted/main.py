from dash import html, dcc 
import dash_bootstrap_components as dbc

from fronted.Navegador.navegador import navegador

layout = dbc.Container(
    [
        dbc.Row(
        [
            dbc.Col(navegador, md = 12, style={'background-color':'mistyrose'})
        ]
         
                ),
        dbc.Row(
            [
                dbc.Col(datos, )

            ]
        )
    ]
)
