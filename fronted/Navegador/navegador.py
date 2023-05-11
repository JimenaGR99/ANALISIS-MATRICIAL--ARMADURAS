from dash import html
import dash_bootstrap_components as dbc


from .Descripcion.armaduras import armaduras


navegador = dbc.Container(
    [
        html.H1('ANÁLISIS MATRICIAL'),
        html.H2('MÉTODO DE LA RIGIDEZ PARA ARMADURAS'),
        dbc.Row(
            [
                dbc.Col(armaduras, md = 12, style={'background-color':'lavender'})

            ]   
                ),
        html.H3('Información a tener en cuenta:'),
        html.Label('*La aplicación calcula fuerzas, desplazamientos y cargas de armaduras compuestas por 3 nodos y 2 elementos'),
        html.Label('*Los nodos se deben ingresar en orden ascendente')


    ]
    
    
)