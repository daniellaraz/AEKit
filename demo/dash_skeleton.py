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
        html.Img(src='/assets/woman1.jpg')
        ], id='subject'),

    html.Div([
        html.Img(src='/assets/woman2.jpg', className='result1', key='0.4')
        ], id='result1'),

    html.Div([
        html.Img(src='/assets/woman3.jpg')
        ], id='result2'),



    html.Div([
        dcc.Slider(
        id='threshold-slider',
        min=0,
        max=5,
        marks={i: str(i/5) for i in range(0, 6)},
        value=1,
    ),
     html.Div(id='slider-output-container')
    ]),



])
@app.callback(
    dash.dependencies.Output('result1', 'style'),
    [dash.dependencies.Input('threshold-slider', 'value')])
def update_output(threshold):
    if threshold/5 == 0.4:
        return {"border":"2px red solid"}
    else:
        return {"border":"2px black solid"}
@app.callback(
    dash.dependencies.Output('result2', 'style'),
    [dash.dependencies.Input('threshold-slider', 'value')])
def update_output(threshold):
    if threshold/5 == 0.4:
        return {"border":"2px red solid"}
    else:
        return {"border":"2px black solid"}




if __name__ == '__main__':
    app.run_server(debug=True)
