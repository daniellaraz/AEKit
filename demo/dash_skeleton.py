import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import pandas as pd
import plotly.graph_objs as go


app = dash.Dash(__name__)


app.layout = html.Div([
    html.Div([
        html.H1('Facial Recognition Bias Demo', id='title'),
        html.P('Welcome to our facial recognition demo. Welcome to our facial recognition demo.Welcome to our facial recognition demo.Welcome to our facial recognition demo.Welcome to our facial recognition demo.Welcome to our facial recognition demo.Welcome to our facial recognition demo.Welcome to our facial recognition demo.Welcome to our facial recognition demo.Welcome to our facial recognition demo.Welcome to our facial recognition demo.Welcome to our facial recognition demo.vWelcome to our facial recognition demo.vWelcome to our facial recognition demo.v', id='intro')
     ]),

    html.Div([

    html.Div([
        html.Img(src='/assets/woman1.jpg')
        ], id='subject'),

    html.Div([
        html.Div([
            html.Img(src='/assets/woman2.jpg', key='0.4', id='img1')
            ], id='result1', className='result1'),

        html.Div([
            html.Img(src='/assets/woman3.jpg', id='img2')
            ], id='result2', className = 'result2'),
            ],
            className = 'box'),




], id='main_wrapper'),
    html.Div([
        dcc.Slider(
        id='threshold-slider',
        min=0,
        max=5,
        marks={i: str(i/5) for i in range(0, 6)},
        value=1,
    )],
     id='slider-output-container', className = 'slider'
    )
])
@app.callback(
    dash.dependencies.Output('img1', 'style'),
    [dash.dependencies.Input('threshold-slider', 'value')])
def update_output(threshold):
    if threshold/5 >=0.4:
        return {"border":"10px red solid"}
    else:
        return {"border":"10px black solid"}
@app.callback(
    dash.dependencies.Output('img2', 'style'),
    [dash.dependencies.Input('threshold-slider', 'value')])
def update_output(threshold):
    if threshold/5 >= 0.2:
        return {"border":"10px red solid"}
    else:
        return {"border":"10px black solid"}




if __name__ == '__main__':
    app.run_server(debug=True)
