import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import pandas as pd
import plotly.graph_objs as go
import math


#add a few people outside of the threshold

app = dash.Dash(__name__)

#read in csv for subject
results = pd.read_csv('/Users/corinnebintz/Desktop/AEKit/AEKit-git/demo/assets/Lisa_Leslie.csv')

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
print(steps)

# upload corresponding images
subject_image = results["Subject_File"][0]
print(subject_image)
images = results["File"]
print(images)
print(images[0])


app.layout = html.Div([
    html.Div([
        html.H1('Facial Recognition False Positive Demo', id='title'),
        html.H2('Instructions:', id='instructions'),
        html.P('Move the slider to change the threshold for the difference between two images that qualifies as a match. If the difference score is  0, the two images are the same. The closer the difference score is to 1 the more different the images are, and the closer the difference score is to 0 the more similar the images are. Matched images are outlined in red.'),
        html.H3("False Positive:"), html.P("When two images result as a match, but aren't actually the same person, a false positive has occurred. Since Lebron James' image is not in the database of images that we compared his image to, any images that result in a match are a false positive. False positive rates from facial recognition technology are higher for people, especially women, of color. Bias in machine learning algorithms can have adverse social effects.")

     ]),

    html.Div([

    html.Div([
        html.Img(src=subject_image, id='celeb'), dcc.RadioItems(
    options=[
        {'label': 'LeBron James', 'value': '/Users/corinnebintz/Desktop/AEKit/AEKit-git/demo/assets/LeBron_James.csv'},
        {'label': 'Lisa Leslie', 'value': '/Users/corinnebintz/Desktop/AEKit/AEKit-git/demo/assets/Lisa_Leslie.csv'}
    ],
    value='/Users/corinnebintz/Desktop/AEKit/AEKit-git/demo/assets/Lisa_Leslie.csv',id = 'subject_options'
)], id='subject'),

    html.Div([
        html.Div([
            html.Img(src=images[0], id='img1')
            ], id='result1', className='result1'),

        html.Div([
            html.Img(src=images[1], id='img2')
            ], id='result2', className = 'result2'),
        html.Div([
            html.Img(src=images[2], id='img3')
            ], id='result3', className = 'result3'),
        html.Div([
            html.Img(src=images[3], id='img4')
            ], id='result4', className = 'result4'),
        html.Div([
            html.Img(src=images[4], id='img5')
            ], id='result5', className = 'result5'),
        html.Div([
            html.Img(src=images[5], id='img6')
            ], id='result6', className = 'result6'),
        html.Div([
            html.Img(src=images[6], id='img7')
            ], id='result7', className = 'result7'),
        html.Div([
            html.Img(src=images[7], id='img8')
            ], id='result8', className = 'result8'),
        html.Div([
            html.Img(src=images[8], id='img9')
            ], id='result9', className = 'result9'),
        html.Div([
            html.Img(src=images[9], id='img10')
            ], id='result10', className = 'result10'),
            ],
            className = 'box'),


], id='main_wrapper'),
    html.Div([
        dcc.Slider(
        id='threshold-slider',
        min=0.0,
        max= threshold_upper,
        step=step,
        value=threshold_upper,
        marks= steps
    )]),

    html.Div(
     id='slider-output-container', className = 'slider'
    )
])


@app.callback(
    dash.dependencies.Output('img1', 'style'),
    [dash.dependencies.Input('threshold-slider', 'value')])
def update_output(threshold):
    if threshold >=similarity[0]:
        return {"border":"10px red solid"}
    else:
        return {"border":"10px black solid"}

@app.callback(
    dash.dependencies.Output('img2', 'style'),
    [dash.dependencies.Input('threshold-slider', 'value')])
def update_output(threshold):
    if threshold >= similarity[1]:
        return {"border":"10px red solid"}
    else:
        return {"border":"10px black solid"}

@app.callback(
    dash.dependencies.Output('img3', 'style'),
    [dash.dependencies.Input('threshold-slider', 'value')])
def update_output(threshold):
    if threshold >= similarity[2]:
        return {"border":"10px red solid"}
    else:
        return {"border":"10px black solid"}

@app.callback(
    dash.dependencies.Output('img4', 'style'),
    [dash.dependencies.Input('threshold-slider', 'value')])
def update_output(threshold):
    if threshold >= similarity[3]:
        return {"border":"10px red solid"}
    else:
        return {"border":"10px black solid"}

@app.callback(
    dash.dependencies.Output('img5', 'style'),
    [dash.dependencies.Input('threshold-slider', 'value')])
def update_output(threshold):
    if threshold >= similarity[4]:
        return {"border":"10px red solid"}
    else:
        return {"border":"10px black solid"}

@app.callback(
    dash.dependencies.Output('img6', 'style'),
    [dash.dependencies.Input('threshold-slider', 'value')])
def update_output(threshold):
    if threshold >= similarity[5]:
        return {"border":"10px red solid"}
    else:
        return {"border":"10px black solid"}

@app.callback(
    dash.dependencies.Output('img7', 'style'),
    [dash.dependencies.Input('threshold-slider', 'value')])
def update_output(threshold):
    if threshold >= similarity[6]:
        return {"border":"10px red solid"}
    else:
        return {"border":"10px black solid"}

@app.callback(
    dash.dependencies.Output('img8', 'style'),
    [dash.dependencies.Input('threshold-slider', 'value')])
def update_output(threshold):
    if threshold >= similarity[7]:
        return {"border":"10px red solid"}
    else:
        return {"border":"10px black solid"}

@app.callback(
    dash.dependencies.Output('img9', 'style'),
    [dash.dependencies.Input('threshold-slider', 'value')])
def update_output(threshold):
    if threshold >= similarity[8]:
        return {"border":"10px red solid"}
    else:
        return {"border":"10px black solid"}

@app.callback(
    dash.dependencies.Output('img10', 'style'),
    [dash.dependencies.Input('threshold-slider', 'value')])
def update_output(threshold):
    if threshold >= similarity[9]:
        return {"border":"10px red solid"}
    else:
        return {"border":"10px black solid"}


@app.callback(
    dash.dependencies.Output('slider-output-container', 'children'),
    [dash.dependencies.Input('threshold-slider', 'value')])
def update_output(value):
    return 'Threshold: You have selected "{}"'.format(value)



#@app.callback(
#    dash.dependencies.Output(results),
#    [dash.dependencies.Input('subject_options', 'value')])
#def update_output(value):
    #return value






if __name__ == '__main__':
    app.run_server(debug=True)
