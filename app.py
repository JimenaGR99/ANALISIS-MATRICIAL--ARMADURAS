    #Se importan las extenxiones a utilizar
import dash
from dash import html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output, State
import json
from fronted.main import layout


    #import backend
from backend.Principal import *


    

ALLOWED_TYPES = (
             "text", "number", "password", "email", "search",
            "tel", "url", "range", "hidden",
        )

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

app.obj=calculo_matriz()
def jsonDefault(object):
    return object.__dict__


app.layout = layout

@app.callback(
    Output('Resultado_general', 'children'), #Muestra la información ingresada por el usuario para cada nodo
    State('value_A', 'value') , #El usuario debe ingresar la cooredenada en x del nodo
    State('value_E', 'value') , #El usuario debe ingresar la cooredenada en y del nodo
    Input('Guardar_general','n_clicks'), #El botón permite generar el almacenamiento de la información del nodo
)

def cargar_general(value_A,value_E,n_clicks):
    n_clicks
    return json.dumps(app.obj.Info_general(value_A,value_E), default=jsonDefault)

@app.callback(
    Output('Resultado_nodo', 'children'), #Muestra la información ingresada por el usuario para cada nodo
    State('value_x', 'value') , #El usuario debe ingresar la cooredenada en x del nodo
    State('value_y', 'value') , #El usuario debe ingresar la cooredenada en y del nodo
    State('value_GLx', 'value') , #El usuario debe ingresar el número del grado de libertad en x del nodo
    State('value_GLy', 'value') , #El usuario debe ingresar el número del grado de libertad en y del nodo
    Input('Guardar_nodo','n_clicks'), #El botón permite generar el almacenamiento de la información del nodo
)

def cargar_nodo(value_x,value_y,value_GLx ,value_GLy,n_clicks):
    n_clicks
    return json.dumps(app.obj.Llenar_datos(value_x,value_y,value_GLx,value_GLy), default=jsonDefault)


@app.callback(
    Output('Resultado_elemento', 'children'),
    State('value_N', 'value') ,
    State('value_F', 'value') ,
    State('value_L', 'value') ,
    Input('Guardar_elemento','n_clicks'),
)
def cargar_elemento(value_N,value_F,value_L,n_clicks):
    n_clicks
    app.aux=app.obj.llenar_elementos(value_N,value_F,value_L)
    if(app.aux==0):
        return json.dumps(app.obj.mostrar_elementos(), default=jsonDefault)

@app.callback(
    Output('Resultado_Apoyos', 'children'),
    Input('Nodo_apoyo', 'value'),
    Input('Apoyo_nuevo', 'n_clicks'),
)
def cargar_Apoyo(Nodo_apoyo, n_clicks):
    n_clicks
    return json.dumps(app.obj.Llenar_Apoyos(Nodo_apoyo), default=jsonDefault)

@app.callback(
    Output('Resultado_matriz', 'children'),
    Input('Calcular','n_clicks'),
)        
def calcular(n_clicks):
    n_clicks
    return json.dumps(app.obj.RealizarCalculo(), default=jsonDefault)


if __name__ == '__main__':
    app.run_server(debug=True)