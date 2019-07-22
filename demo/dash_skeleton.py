import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import pandas as pd
import plotly.graph_objs as go


app = dash.Dash()


app.layout = html.Div([
    html.Div([
        html.H1('Facial Recognition Bias Demo', id='title'),
        html.P('Welcome to our facial recognition demo. Welcome to our facial recognition demo.Welcome to our facial recognition demo.Welcome to our facial recognition demo.Welcome to our facial recognition demo.Welcome to our facial recognition demo.Welcome to our facial recognition demo.Welcome to our facial recognition demo.Welcome to our facial recognition demo.Welcome to our facial recognition demo.Welcome to our facial recognition demo.Welcome to our facial recognition demo.vWelcome to our facial recognition demo.vWelcome to our facial recognition demo.v', id='intro')

     ]),



    html.Div([
        html.Img(src='/assets/woman1.jpg')
        ]),

    html.Div([
        html.Img(src='/assets/woman2.jpg')
        ]),

    html.Div([
        html.Img(src='/assets/woman3.jpg')
        ]),


     html.Div([
        dcc.Upload(
        id='upload-data',
        children=html.Div([
            'Drag and Drop or ',
            html.A('Select Files')
        ]),
        style={
            'width': '100%',
            'height': '60px',
            'lineHeight': '60px',
            'borderWidth': '1px',
            'borderStyle': 'dashed',
            'borderRadius': '5px',
            'textAlign': 'center',
            'margin': '10px'
        },
        # Allow multiple files to be uploaded
        multiple=True
    ),
    html.Div(id='output-data-upload'),

      ]),

    html.Div([
        dcc.Slider(
        min=-5,
        max=10,
        marks={i: 'Label {}'.format(i) for i in range(10)},
        value=-3

    ),

    ]),


])


if __name__ == '__main__':
    app.run_server(debug=True)
