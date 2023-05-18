from dash import html
import dash_bootstrap_components as dbc


from .Descripcion.armaduras import *


navegador = dbc.Container(
    [
        html.H1('ANÁLISIS MATRICIAL'),  
        html.H2('MÉTODO DE LA RIGIDEZ PARA ARMADURAS'),
        dbc.Row(
            [
                dbc.Col(armaduras, md = 12, style={'background-color':'#F3CCFF'}), #Se agrega una breve descripción del método de armaduras
                dbc.Col(Informacion_importante, md = 12, style={'background-color':'#ffab74'})

            ]   
                ),
        

    ]
    
    
)