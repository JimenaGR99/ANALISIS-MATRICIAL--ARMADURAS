    #Se importan las librerías que se utilizarán
from dash import html, dcc
import dash_bootstrap_components as dbc



Informacion_general = dbc.Container(
    [

         html.Div(
          [
              dbc.Col(
                [
               
                    html.H1('Información General'),
                    dcc.Input(id='value_A', type='number', placeholder='Área de la sección transversal', className='form-control'), #El usuario ingresa el área de la sección transversal
                    dcc.Input(id='value_E', type='number', placeholder='Módulo de elasticidad', className='form-control'), #El usuario ingresa el valor del módulo de elasticidad
                    html.Button('Guardar', id='Guardar_general', n_clicks=0, className='btn btn-info',style={'margin-top':'10px'}), #Se crea el botón mediante el cuál se guarda la información de cada elemento
                    html.Div(id='Resultado_general'),
                ],md=11,className='form-group' ,style={})
          ]
         )
    ]
)

Informacion_nodos = dbc.Container(
    [
              
        html.Div(
          [
              dbc.Col(
                [
                    html.H1('Nodos'),
                    dcc.Input(id='value_x', type='number', placeholder='Ingrese coordenada en x',className='form-control'),
                    dcc.Input(id='value_y', type='number', placeholder='Ingrese coordenada en y',className='form-control'),
                    dcc.Input(id='value_GLx', type='number', placeholder='Grado de libertad en X',className='form-control'),
                    dcc.Input(id='value_GLy', type='number', placeholder='Grado de libertad en Y',className='form-control'),
                    html.Button('Guardar', id='Guardar_nodo', n_clicks=0, className='btn btn-info', style={'margin-top':'10px'}),
                    html.Div(id='Resultado_nodo'),
                ],md=11, className='Form-group' ,style={})
          ], 
        ),
        
    ]
)

Informacion_elementos = dbc.Container(
    [
        # ingresar 2 elementos
        # nodo inicio
        # nodo final
        # longitud
        html.Div(
           [
               dbc.Col(
                [
               
                    html.H1('Elementos'),
                    dcc.Input(id='value_N', type='number', placeholder='Nodo inicial', className='form-control'), #El usuario ingresa el número del nodo inicial del elemento
                    dcc.Input(id='value_F', type='number', placeholder='Nodo Final', className='form-control'), #El usuario ingresa el número del nodo final del elemento
                    dcc.Input(id='value_L', type='number', placeholder='Longitud', className='form-control'), #El usuario ingresa la longitud del elemento
                    html.Button('Guardar', id='Guardar_elemento', n_clicks=0, className='btn btn-info',style={'margin-top':'10px'}), #Se crea el botón mediante el cuál se guarda la información de cada elemento
                    html.Div(id='Resultado_elemento'),
                ],md=11,className='form-group' ,style={})
           ]  
        ) 
    ]
)
Apoyos = dbc.Container(
    [
              
        html.Div(
          [
              dbc.Col(
                [
                    html.H1('Apoyos de la armadura'),
                    dcc.Input(id='Nodo_apoyo', type='number', placeholder='Ingrese el nodo en dónde se presentan los apoyos',className='form-control'),
                    html.Button('Guardar', id='Apoyo_nuevo', n_clicks=0, className='btn btn-info', style={'margin-top':'10px'}),
                    html.Div(id='Resultado_Apoyos'),
                ],md=11, className='Form-group' ,style={})
          ], 
        ),
        
    ]
)
Cargas_conocidas = dbc.Container(
    [
              
        html.Div(
          [
              dbc.Col(
                [
                    html.H1('Cargas Conocidas'),
                    dcc.Input(id='Carga_conocida', type='number', placeholder='Ingrese la carga aplicada',className='form-control'),
                    dcc.Input(id='GL_con_carga', type='number', placeholder='Ingrese el GL dónde se aplica la carga',className='form-control'),
                    html.Button('Guardar', id='Guardar_nodo', n_clicks=0, className='btn btn-info', style={'margin-top':'10px'}),
                    html.Div(id='Resultado_cargas'),
                ],md=11, className='Form-group' ,style={})
          ], 
        ),
        
    ]
)
Calculo_matriz_total = dbc.Container(
    [

         html.Div(
          [
              dbc.Col(
                [
                    html.Button('Calcular', id='Calcular', n_clicks=0, className='btn btn-primary', style={'margin-left':'95%'}),
                    html.Div(id='Resultado_matriz'),
                ],md=11
              )
          ]
         )
    ]
)