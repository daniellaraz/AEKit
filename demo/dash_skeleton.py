import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import pandas as pd
import plotly.graph_objs as go
import math


#add a few people outside of the threshold

app = dash.Dash(__name__)


def load_data(csv):
    #read in csv for subject

    results = pd.read_csv(csv)


    #determine max similarity
    similarity = results['Similarity']
    max_sim = max(similarity)

    #determine upper limit for threshold rounded to nearest 0.5
    threshold_upper = math.ceil(max_sim*2)/2

    #determine step for threshold
    step = threshold_upper/10

    #create mark dictionary for slider
    steps = {}
    c=0
    for i in range(11):
        if round((c+step*i), 2) == 0.00:
            steps[0] = str(round(c+(step*i), 1))
        elif round((c+step*i), 2) == 1.00:
            steps[1] = str(round(c+(step*i), 1))
        else:
            steps[round((c+step*i), 2)] = str(round(c+(step*i), 2))

    # upload corresponding images
    subject_image = results["Subject_File"][0]
    images = results["File"]

original_csv = '/Users/corinnebintz/Desktop/AEKit/AEKit-git/demo/assets/Lisa_Leslie.csv'


app.layout = html.Div([
    html.Div([
        html.H1('Facial Recognition False Positive Demo', id='title'),
        html.H2('Instructions:', id='instructions'),
        html.P('Move the slider to change the threshold for the difference between two images that qualifies as a match. If the difference score is  0, the two images are the same. The closer the difference score is to 1 the more different the images are, and the closer the difference score is to 0 the more similar the images are. Matched images are outlined in red.'),
        html.H3("False Positive:"), html.P("When two images result as a match, but aren't actually the same person, a false positive has occurred. Since Lebron James' image is not in the database of images that we compared his image to, any images that result in a match are a false positive. False positive rates from facial recognition technology are higher for people, especially women, of color. Bias in machine learning algorithms can have adverse social effects.")

     ]),

    html.Div([

    html.Div([
        html.Img(id='celeb'), dcc.RadioItems(
    options=[
        {'label': 'LeBron James', 'value': '/Users/corinnebintz/Desktop/AEKit/AEKit-git/demo/assets/LeBron_James.csv'},
        {'label': 'Lisa Leslie', 'value': '/Users/corinnebintz/Desktop/AEKit/AEKit-git/demo/assets/Lisa_Leslie.csv'}
    ],
    value='/Users/corinnebintz/Desktop/AEKit/AEKit-git/demo/assets/Lisa_Leslie.csv',id = 'subject_options'
)], id='subject'),

    html.Div([
        html.Div([
            html.Img(id='img1')
            ], id='result1', className='result1'),

        html.Div([
            html.Img(id='img2')
            ], id='result2', className = 'result2'),
        html.Div([
            html.Img(id='img3')
            ], id='result3', className = 'result3'),
        html.Div([
            html.Img(id='img4')
            ], id='result4', className = 'result4'),
        html.Div([
            html.Img(id='img5')
            ], id='result5', className = 'result5'),
        html.Div([
            html.Img(id='img6')
            ], id='result6', className = 'result6'),
        html.Div([
            html.Img(id='img7')
            ], id='result7', className = 'result7'),
        html.Div([
            html.Img(id='img8')
            ], id='result8', className = 'result8'),
        html.Div([
            html.Img(id='img9')
            ], id='result9', className = 'result9'),
        html.Div([
            html.Img(id='img10')
            ], id='result10', className = 'result10'),
            ],
            className = 'box'),


], id='main_wrapper'),
    html.Div([
        dcc.Slider(
        id='threshold-slider',
        min=0.0
    )]),

    html.Div(
     id='slider-output-container', className = 'slider'
    )
])

#load all images
#and slider
#TOOKOUT MARKS FOR NOW
#TOOKOUT VALUES FOR NOW

@app.callback([Output('celeb', 'src'), Output('img1', 'src'), Output('img2', 'src'), Output('img3', 'src'), Output('img4', 'src'), Output('img5', 'src'),
Output('img6', 'src'), Output('img7', 'src'), Output('img8', 'src'), Output('img9', 'src'), Output('img10', 'src'), Output('threshold-slider', 'max'), Output('threshold-slider', 'step')],
    [Input('subject_options', 'value')])
def update_output(value):
    #data = load_data(value)
    results = pd.read_csv(value)


    #determine max similarity
    similarity = results['Similarity']
    max_sim = max(similarity)

    #determine upper limit for threshold rounded to nearest 0.5
    threshold_upper = math.ceil(max_sim*2)/2

    #determine step for threshold
    step = threshold_upper/10

    #create mark dictionary for slider
    steps = {}
    c=0
    for i in range(11):
        if round((c+step*i), 2) == 0.00:
            steps[0] = str(round(c+(step*i), 1))
        elif round((c+step*i), 2) == 1.00:
            steps[1] = str(round(c+(step*i), 1))
        else:
            steps[round((c+step*i), 2)] = str(round(c+(step*i), 2))

    # upload corresponding images
    subject_image = results["Subject_File"][0]
    images = results["File"]


    return subject_image, images[0], images[1], images[2], images[3], images[4], images[5], images[6], images[7], images[8], images[9], threshold_upper, step


# @app.callback(
#     dash.dependencies.Output('img1', 'style'),
#     [dash.dependencies.Input('threshold-slider', 'value')])
# def update_output(threshold):
#     if threshold >=similarity[0]:
#         return {"border":"10px red solid"}
#     else:
#         return {"border":"10px black solid"}
#
# @app.callback(
#     dash.dependencies.Output('img2', 'style'),
#     [dash.dependencies.Input('threshold-slider', 'value')])
# def update_output(threshold):
#     if threshold >= similarity[1]:
#         return {"border":"10px red solid"}
#     else:
#         return {"border":"10px black solid"}
#
# @app.callback(
#     dash.dependencies.Output('img3', 'style'),
#     [dash.dependencies.Input('threshold-slider', 'value')])
# def update_output(threshold):
#     if threshold >= similarity[2]:
#         return {"border":"10px red solid"}
#     else:
#         return {"border":"10px black solid"}
#
# @app.callback(
#     dash.dependencies.Output('img4', 'style'),
#     [dash.dependencies.Input('threshold-slider', 'value')])
# def update_output(threshold):
#     if threshold >= similarity[3]:
#         return {"border":"10px red solid"}
#     else:
#         return {"border":"10px black solid"}
#
# @app.callback(
#     dash.dependencies.Output('img5', 'style'),
#     [dash.dependencies.Input('threshold-slider', 'value')])
# def update_output(threshold):
#     if threshold >= similarity[4]:
#         return {"border":"10px red solid"}
#     else:
#         return {"border":"10px black solid"}
#
# @app.callback(
#     dash.dependencies.Output('img6', 'style'),
#     [dash.dependencies.Input('threshold-slider', 'value')])
# def update_output(threshold):
#     if threshold >= similarity[5]:
#         return {"border":"10px red solid"}
#     else:
#         return {"border":"10px black solid"}
#
# @app.callback(
#     dash.dependencies.Output('img7', 'style'),
#     [dash.dependencies.Input('threshold-slider', 'value')])
# def update_output(threshold):
#     if threshold >= similarity[6]:
#         return {"border":"10px red solid"}
#     else:
#         return {"border":"10px black solid"}
#
# @app.callback(
#     dash.dependencies.Output('img8', 'style'),
#     [dash.dependencies.Input('threshold-slider', 'value')])
# def update_output(threshold):
#     if threshold >= similarity[7]:
#         return {"border":"10px red solid"}
#     else:
#         return {"border":"10px black solid"}
#
# @app.callback(
#     dash.dependencies.Output('img9', 'style'),
#     [dash.dependencies.Input('threshold-slider', 'value')])
# def update_output(threshold):
#     if threshold >= similarity[8]:
#         return {"border":"10px red solid"}
#     else:
#         return {"border":"10px black solid"}
#
# @app.callback(
#     dash.dependencies.Output('img10', 'style'),
#     [dash.dependencies.Input('threshold-slider', 'value')])
# def update_output(threshold):
#     if threshold >= similarity[9]:
#         return {"border":"10px red solid"}
#     else:
#         return {"border":"10px black solid"}
#
#
# @app.callback(
#     dash.dependencies.Output('slider-output-container', 'children'),
#     [dash.dependencies.Input('threshold-slider', 'value')])
# def update_output(value):
#     return 'Threshold: You have selected "{}"'.format(value)










if __name__ == '__main__':
    app.run_server(debug=True)
