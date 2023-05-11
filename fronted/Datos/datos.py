from dash import html, dcc
import dash_bootstrap_components as dbc


Informacion_general = dbc.Container(
    [
        #Area seccion transversal
        #Modulo de elasticidad
    ]
)

Informacion_nodos = dbc.Container(
    [
              
        html.Div(
            [
                html.H1('   x  Y   GL X   GL Y'),
                dcc.Input(id="value_x", type="number", placeholder="Ingrese coordenada x"),
                dcc.Input(id="value_y", type="number", placeholder="Ingrese coordenada y "),
                dcc.Input(id="value_GLx", type="number", placeholder="Grado de libertad X "),
                dcc.Input(id="value_GLy", type="number", placeholder="grado de libertad Y "),
            ]
        )
        #ingresar 2 elementos 
    ]
)

Informacion_elementos = dbc.Container(
    [
        # ingresar 2 elementos
        # nodo inicio
        # nodo final
        # longitud
    ]
)
