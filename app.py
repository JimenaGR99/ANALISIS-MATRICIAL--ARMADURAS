import dash
from dash import html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output

from fronted.main import layout

#import backend
from backend.Principal import *

ALLOWED_TYPES = (
             "text", "number", "password", "email", "search",
            "tel", "url", "range", "hidden",
        )

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

app.layout = layout

@app.callback(
    Output("out-all-types", "children"),
    [Input("value_x", "value") for _ in ALLOWED_TYPES],
    [Input("value_y", "value") for _ in ALLOWED_TYPES],
    [Input("value_GLx", "value") for _ in ALLOWED_TYPES],
    [Input("value_GLy", "value") for _ in ALLOWED_TYPES],
)

def ingresar_dato():
    aux=calculo_matriz()


if __name__ == '__main__':
    app.run_server(debug=True)