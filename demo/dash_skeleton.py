import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import pandas as pd
import plotly.graph_objs as go


app = dash.Dash(__name__)

#read in csv for subject
results = pd.read_csv('/Users/corinnebintz/Desktop/AEKit/AEKit-git/demo/assets/LeBron_James.csv'),


app.layout = html.Div([
    html.Div([
        html.H1('Facial Recognition False Positive Demo', id='title'),
        html.H2('Instructions:', id='instructions'),
        html.P('Move the slider to change the threshold for the difference between two images that qualifies as a match. If the difference score is  0, the two images are the same. The closer the difference score is to 1 the more different the images are, and the closer the difference score is to 0 the more similar the images are. Matched images are outlined in red.'),
        html.H3("False Positive:"), html.P("When two images result as a match, but aren't actually the same person, a false positive has occurred. Since Lebron James' image is not in the database of images that we compared his image to, any images that result in a match are a false positive. False positive rates from facial recognition technology are higher for people, especially women, of color. Bias in machine learning algorithms can have adverse social effects.")

     ]),

    html.Div([

    html.Div([
        html.Img(src='/assets/LeBron_James_0002.jpg', id='lebron')
        ], id='subject'),

    html.Div([
        html.Div([
            html.Img(src='/assets/Jacqueline_Edwards_0001.jpg', id='img1')
            ], id='result1', className='result1'),

        html.Div([
            html.Img(src='/assets/Jason_Campbell_0001.jpg', id='img2')
            ], id='result2', className = 'result2'),
        html.Div([
            html.Img(src='/assets/Jennette_Bradley_0001.jpg', id='img3')
            ], id='result3', className = 'result3'),
        html.Div([
            html.Img(src='/assets/Julian_Battle_0001.jpg', id='img4')
            ], id='result4', className = 'result4'),
        html.Div([
            html.Img(src='/assets/Julius_Erving_0001.jpg', id='img5')
            ], id='result5', className = 'result5'),
        html.Div([
            html.Img(src='/assets/Kelli_White_0002.jpg', id='img6')
            ], id='result6', className = 'result6'),
        html.Div([
            html.Img(src='/assets/Kobe_Bryant_0003.jpg', id='img7')
            ], id='result7', className = 'result7'),
        html.Div([
            html.Img(src='/assets/Kwame_Kilpatrick_0001.jpg', id='img8')
            ], id='result8', className = 'result8'),
        html.Div([
            html.Img(src='/assets/Larry_Thompson_0001.jpg', id='img9')
            ], id='result9', className = 'result9'),
        html.Div([
            html.Img(src='/assets/Marquis_Estill_0001.jpg', id='img10')
            ], id='result10', className = 'result10'),
            ],
            className = 'box'),


], id='main_wrapper'),
    html.Div([
        dcc.Slider(
        id='threshold-slider',
        min=0,
        max=1.0,
        step=0.1,
        value=1,
        marks={
        0: '0',
        0.1: '0.1',
        0.2: '0.2',
        0.3: '0.3',
        0.4: '0.4',
        0.5: '0.5',
        0.6: '0.6',
        0.7: '0.7',
        0.8: '0.8',
        0.9: '0.9',
        1: '1.0'
    },

    )]),

    html.Div(
     id='slider-output-container', className = 'slider'
    )
])

#Jacqueline_Edwards_0001 0.819
@app.callback(
    dash.dependencies.Output('img1', 'style'),
    [dash.dependencies.Input('threshold-slider', 'value')])
def update_output(threshold):
    if threshold >=0.819:
        return {"border":"10px red solid"}
    else:
        return {"border":"10px black solid"}

#Jason_Campbell_0001 0.806
@app.callback(
    dash.dependencies.Output('img2', 'style'),
    [dash.dependencies.Input('threshold-slider', 'value')])
def update_output(threshold):
    if threshold >= 0.806:
        return {"border":"10px red solid"}
    else:
        return {"border":"10px black solid"}

#Jennette_Bradley_0001 0.977
@app.callback(
    dash.dependencies.Output('img3', 'style'),
    [dash.dependencies.Input('threshold-slider', 'value')])
def update_output(threshold):
    if threshold >= 0.977:
        return {"border":"10px red solid"}
    else:
        return {"border":"10px black solid"}

#Julian_Battle_0001 0.655
@app.callback(
    dash.dependencies.Output('img4', 'style'),
    [dash.dependencies.Input('threshold-slider', 'value')])
def update_output(threshold):
    if threshold >= 0.655:
        return {"border":"10px red solid"}
    else:
        return {"border":"10px black solid"}

#Julius_Erving_0001 0.724
@app.callback(
    dash.dependencies.Output('img5', 'style'),
    [dash.dependencies.Input('threshold-slider', 'value')])
def update_output(threshold):
    if threshold >= 0.724:
        return {"border":"10px red solid"}
    else:
        return {"border":"10px black solid"}

#Kelli_White_0002 0.919
@app.callback(
    dash.dependencies.Output('img6', 'style'),
    [dash.dependencies.Input('threshold-slider', 'value')])
def update_output(threshold):
    if threshold >= 0.919:
        return {"border":"10px red solid"}
    else:
        return {"border":"10px black solid"}

#Kobe_Bryant_0003 0.825
@app.callback(
    dash.dependencies.Output('img7', 'style'),
    [dash.dependencies.Input('threshold-slider', 'value')])
def update_output(threshold):
    if threshold >= 0.825:
        return {"border":"10px red solid"}
    else:
        return {"border":"10px black solid"}

#Kwame_Kilpatrick_0001 0.442
@app.callback(
    dash.dependencies.Output('img8', 'style'),
    [dash.dependencies.Input('threshold-slider', 'value')])
def update_output(threshold):
    if threshold >= 0.442:
        return {"border":"10px red solid"}
    else:
        return {"border":"10px black solid"}

#Larry_Thompson_0001 0.151
@app.callback(
    dash.dependencies.Output('img9', 'style'),
    [dash.dependencies.Input('threshold-slider', 'value')])
def update_output(threshold):
    if threshold >= 0.151:
        return {"border":"10px red solid"}
    else:
        return {"border":"10px black solid"}

#Marquis_Estill_0001 0.719
@app.callback(
    dash.dependencies.Output('img10', 'style'),
    [dash.dependencies.Input('threshold-slider', 'value')])
def update_output(threshold):
    if threshold >= 0.719:
        return {"border":"10px red solid"}
    else:
        return {"border":"10px black solid"}


@app.callback(
    dash.dependencies.Output('slider-output-container', 'children'),
    [dash.dependencies.Input('threshold-slider', 'value')])
def update_output(value):
    return 'Threshold: You have selected "{}"'.format(value)





if __name__ == '__main__':
    app.run_server(debug=True)
