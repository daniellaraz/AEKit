import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import pandas as pd
import plotly.graph_objs as go
import math


#add a few people outside of the threshold

app = dash.Dash(__name__)
app.title = 'Facial Recognition Demo'


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

    html.Div([ html.Div(id='current_data_similarity', style={'display': 'none'}, children=[0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0]),
    html.Div(id='current_data_names', style={'display': 'none'}, children=['','','','','','','','','','']),

    html.Div([
        html.Img(id='celeb'), dcc.RadioItems(
    options=[
        {'label': 'LeBron James', 'value': '/Users/corinnebintz/Desktop/AEKit/AEKit-git/demo/assets/LeBron_James.csv'},
        {'label': 'Lisa Leslie', 'value': '/Users/corinnebintz/Desktop/AEKit/AEKit-git/demo/assets/Lisa_Leslie.csv'},
        {'label': 'Paris Hilton', 'value': '/Users/corinnebintz/Desktop/AEKit/AEKit-git/demo/assets/Paris_Hilton.csv'},
        {'label': 'Aaron Peirsol', 'value': '/Users/corinnebintz/Desktop/AEKit/AEKit-git/demo/assets/Aaron_Peirsol.csv'},
        {'label': 'Jacqueline Edwards', 'value': '/Users/corinnebintz/Desktop/AEKit/AEKit-git/demo/assets/Jacqueline_Edwards.csv'},
        {'label': 'Kalpana Chawla', 'value': '/Users/corinnebintz/Desktop/AEKit/AEKit-git/demo/assets/Kalpana_Chawla.csv'},
        {'label': 'Jason Campbell', 'value': '/Users/corinnebintz/Desktop/AEKit/AEKit-git/demo/assets/Jason_Campbell.csv'},
        {'label': 'Katie Couric', 'value': '/Users/corinnebintz/Desktop/AEKit/AEKit-git/demo/assets/Katie_Couric.csv'},
        {'label': 'Vicki Zhao Wei', 'value': '/Users/corinnebintz/Desktop/AEKit/AEKit-git/demo/assets/Vicki_Zhao_Wei.csv'}
    ],
    value='/Users/corinnebintz/Desktop/AEKit/AEKit-git/demo/assets/Lisa_Leslie.csv',id = 'subject_options'
)], id='subject'),

    html.Div([
        html.Div([
            html.Img(id='img1'), html.Figcaption(id='name1'),
            html.Figcaption(id='sim1')
            ], id='result1', className='result1'),

        html.Div([
            html.Img(id='img2'), html.Figcaption(id='name2'),
            html.Figcaption(id='sim2')
            ], id='result2', className = 'result2'),
        html.Div([
            html.Img(id='img3'), html.Figcaption(id='name3'),
            html.Figcaption(id='sim3')
            ], id='result3', className = 'result3'),
        html.Div([
            html.Img(id='img4'), html.Figcaption(id='name4'),
            html.Figcaption(id='sim4')
            ], id='result4', className = 'result4'),
        html.Div([
            html.Img(id='img5'), html.Figcaption(id='name5'),
            html.Figcaption(id='sim5')
            ], id='result5', className = 'result5'),
        html.Div([
            html.Img(id='img6'), html.Figcaption(id='name6'),
            html.Figcaption(id='sim6')
            ], id='result6', className = 'result6'),
        html.Div([
            html.Img(id='img7'), html.Figcaption(id='name7'),
            html.Figcaption(id='sim7')
            ], id='result7', className = 'result7'),
        html.Div([
            html.Img(id='img8'), html.Figcaption(id='name8'),
            html.Figcaption(id='sim8')
            ], id='result8', className = 'result8'),
        html.Div([
            html.Img(id='img9'), html.Figcaption(id='name9'),
            html.Figcaption(id='sim9')
            ], id='result9', className = 'result9'),
        html.Div([
            html.Img(id='img10'), html.Figcaption(id='name10'),
            html.Figcaption(id='sim10')
            ], id='result10', className = 'result10'),
            ],
            className = 'box'),


], id='main_wrapper'),
    html.Div([
        dcc.Slider(
        id='threshold-slider',
        min=0.0,
        value = 0.0
    )]),

    html.Div(
     id='slider-output-container', className = 'slider'
    )
])

#load all images
#and slider

@app.callback([Output('celeb', 'src'), Output('img1', 'src'), Output('img2', 'src'), Output('img3', 'src'), Output('img4', 'src'), Output('img5', 'src'),
Output('img6', 'src'), Output('img7', 'src'), Output('img8', 'src'), Output('img9', 'src'), Output('img10', 'src'), Output('threshold-slider', 'max'), Output('threshold-slider', 'step'),
Output('threshold-slider', 'marks'), Output('threshold-slider', 'value'), Output('current_data_similarity', 'children'), Output('current_data_names', 'children')], [Input('subject_options', 'value')])
def update_output(value):
    #data = load_data(value)
    results = pd.read_csv(value)

    #gather names
    names = results['Name']

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

    return [subject_image, images[0], images[1], images[2], images[3], images[4],
        images[5], images[6], images[7], images[8], images[9], threshold_upper,
        step, steps, threshold_upper, similarity, names]

# threshold image 1
@app.callback([Output('img1', 'style'), Output('name1', 'children'), Output('sim1', 'children')],
    [Input('threshold-slider', 'value'), Input('current_data_similarity', 'children'), Input('current_data_names', 'children')])
def update_output(threshold, similarity, names):
    if threshold >= similarity[0]:
        return {"border":"10px red solid"}, names[0], str(round(similarity[0], 3))
    else:
        return {"border":"10px black solid"}, names[0], str(round(similarity[0], 3))

#threshold image 2
@app.callback([Output('img2', 'style'),Output('name2', 'children'), Output('sim2', 'children')],
    [Input('threshold-slider', 'value'), Input('current_data_similarity', 'children'), Input('current_data_names', 'children')])
def update_output(threshold, similarity, names):
    if threshold >= similarity[1]:
        return {"border":"10px red solid"}, names[1], str(round(similarity[1], 3))
    else:
        return {"border":"10px black solid"}, names[1], str(round(similarity[1], 3))

#threshold image 3
@app.callback([Output('img3', 'style'),Output('name3', 'children'), Output('sim3', 'children')],
    [Input('threshold-slider', 'value'), Input('current_data_similarity', 'children'), Input('current_data_names', 'children')])
def update_output(threshold, similarity, names):
    if threshold >= similarity[2]:
        return {"border":"10px red solid"}, names[2], str(round(similarity[2], 3))
    else:
        return {"border":"10px black solid"}, names[2], str(round(similarity[2], 3))

#threshold image 4
@app.callback([Output('img4', 'style'),Output('name4', 'children'), Output('sim4', 'children')],
    [Input('threshold-slider', 'value'), Input('current_data_similarity', 'children'), Input('current_data_names', 'children')])
def update_output(threshold, similarity, names):
    if threshold >= similarity[3]:
        return {"border":"10px red solid"}, names[3], str(round(similarity[3], 3))
    else:
        return {"border":"10px black solid"}, names[3], str(round(similarity[3], 3))

#threshold image 5
@app.callback([Output('img5', 'style'),Output('name5', 'children'), Output('sim5', 'children')],
    [Input('threshold-slider', 'value'), Input('current_data_similarity', 'children'), Input('current_data_names', 'children')])
def update_output(threshold, similarity, names):
    if threshold >= similarity[4]:
        return {"border":"10px red solid"}, names[4], str(round(similarity[4], 3))
    else:
        return {"border":"10px black solid"}, names[4], str(round(similarity[4], 3))

#threshold image 6
@app.callback([Output('img6', 'style'),Output('name6', 'children'), Output('sim6','children')],
    [Input('threshold-slider', 'value'), Input('current_data_similarity', 'children'), Input('current_data_names', 'children')])
def update_output(threshold, similarity, names):
    if threshold >= similarity[5]:
        return {"border":"10px red solid"}, names[5], str(round(similarity[5], 3))
    else:
        return {"border":"10px black solid"}, names[5], str(round(similarity[5], 3))

#threshold image 7
@app.callback([Output('img7', 'style'),Output('name7', 'children'), Output('sim7', 'children')],
    [Input('threshold-slider', 'value'), Input('current_data_similarity', 'children'), Input('current_data_names', 'children')])
def update_output(threshold, similarity, names):
    if threshold >= similarity[6]:
        return {"border":"10px red solid"}, names[6], str(round(similarity[6], 3))
    else:
        return {"border":"10px black solid"}, names[6], str(round(similarity[6], 3))

#threshold image 8
@app.callback([Output('img8', 'style'),Output('name8', 'children'), Output('sim8', 'children')],
    [Input('threshold-slider', 'value'), Input('current_data_similarity', 'children'), Input('current_data_names', 'children')])
def update_output(threshold, similarity, names):
    if threshold >= similarity[7]:
        return {"border":"10px red solid"}, names[7], str(round(similarity[7], 3))
    else:
        return {"border":"10px black solid"}, names[7], str(round(similarity[7], 3))

#threshold image 9
@app.callback([Output('img9', 'style'),Output('name9', 'children'), Output('sim9', 'children')],
    [Input('threshold-slider', 'value'), Input('current_data_similarity', 'children'), Input('current_data_names', 'children')])
def update_output(threshold, similarity, names):
    if threshold >= similarity[8]:
        return {"border":"10px red solid"}, names[8], str(round(similarity[8], 3))
    else:
        return {"border":"10px black solid"}, names[8], str(round(similarity[8], 3))

#threshold image 10
@app.callback([Output('img10', 'style'),Output('name10', 'children'), Output('sim10', 'children')],
    [Input('threshold-slider', 'value'), Input('current_data_similarity', 'children'), Input('current_data_names', 'children')])
def update_output(threshold, similarity, names):
    if threshold >= similarity[9]:
        return {"border":"10px red solid"}, names[9], str(round(similarity[9], 3))
    else:
        return {"border":"10px black solid"}, names[9], str(round(similarity[9], 3))

@app.callback(
    dash.dependencies.Output('slider-output-container', 'children'),
    [dash.dependencies.Input('threshold-slider', 'value')])
def update_output(value):
    return 'Threshold: You have selected "{}"'.format(value)

# @app.callback(
#     dash.dependencies.Output('subject', 'children'),
#     [dash.dependencies.Input('celeb', 'n_clicks')])
# def update_output(clicks):
#     if clicks != None:
#         return 'Clicked!'



if __name__ == '__main__':
    app.run_server(debug=True)
