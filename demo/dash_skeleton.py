import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import pandas as pd
import plotly.graph_objs as go
import math

# green = true match -DONE
# add another picture into database -DONE
# change 1-x for similarity scores - DONE
# less similar (0.0) to more similar (1.5) -DONE
# use "similar score" instead of "difference score" -DONE
# closest match is green, everything above threshold but not closet is yellow -DONE
# black for those below threshold - DONE
# add things to look out for -DONE
# steps in instructions -DONE


#add a few people outside of the threshold (?)

app = dash.Dash(__name__)
app.title = 'Facial Recognition Demo'


# introduction text
app.layout = html.Div([
    html.Div([
        html.H3('Facial Recognition False Positive Demo', id='title'),
        html.H4('Instructions:', id='instructions'),
        html.P("1. Enter full screen in your browser. Listed below each celebrity name is the similarity score that resulted from comparing that image to the current subject using open source facial recognition software."),
        html.Div([
    "2. Move the slider by clicking on the number intervals to change the minimum similarity required between the subject and each image to qualify as a match, which we refer to as the",
    html.Span(" threshold. ", style = {"font-weight": "bold"}),
    "The larger the similarity score is, the more similar two images are. We refer to images that match according to the similarity threshold, but aren't really the same person, as ",
    html.Span('false positives. False positives ', style={'font-weight': 'bold'}),
    'are outlined in ',
    html.Span('yellow', style={'background-color': 'yellow', 'font-weight': 'bold'}),
    '. When the images match and are truly the same person, we call this a  ',
    html.Span('true match. True matches ', style={'font-weight': 'bold'}),
    'are outlined in ',
    html.Span('green', style={'background-color': '#98FB98', 'font-weight': 'bold'}),
    ". We refer to images with similarity scores that fall below the threshold and don't match as ",
    html.Span('non-matches. Non-matches ', style={'font-weight': 'bold'}),
    'are outlined in ',
    html.Span('black.', style={'font-weight': 'bold'}),
    ' Explore each interval of the threshold slider to see how false positives, true matches, and non-matches change depending on the threshold.'

]),
        html.P("3. Notice differences in similarity scores of the 10 images for subjects of different skin tones and genders. Research shows facial recognition software to have lower accuracy for people, especially women, of color. For instance, notice how when Jacqueline Edwards is the subject, Kelly White has a higher simliarity score to Jacqueline Edwards than a different picture of Jacqueline Edwards to herself. The racial and gender disparities in accuracy of facial recognition technology can result in negative societal impacts when implementing the technology for surveillance or policing purposes."),
        html.P("4. Analyze a different subject by choosing from the subject options on the left side of the demo.")

     ]),

    # stores current subject data
    html.Div([ html.Div(id='current_data_similarity', style={'display': 'none'}, children=[0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0]),
    html.Div(id='current_data_names', style={'display': 'none'}, children=['','','','','','','','','','']),
    html.Div(id='current_match_values', style={'display': 'none'}, children=[False,False,False,False,False,False,False,False,False,False]),

    # subject and radio button options to switch subject
    html.Div([
        html.H4('Current subject'),
        html.Img(id='celeb'), dcc.RadioItems(
    options=[
        {'label': 'LeBron James', 'value': 'LeBron_James.csv'},
        {'label': 'Lisa Leslie', 'value': 'Lisa_Leslie.csv'},
        {'label': 'Paris Hilton', 'value': 'Paris_Hilton.csv'},
        {'label': 'Aaron Peirsol', 'value': 'Aaron_Peirsol.csv'},
        {'label': 'Jacqueline Edwards', 'value': 'Jacqueline_Edwards.csv'},
        {'label': 'Kalpana Chawla', 'value': 'Kalpana_Chawla.csv'},
        {'label': 'Jason Campbell', 'value': 'Jason_Campbell.csv'},
        {'label': 'Katie Couric', 'value': 'Katie_Couric.csv'},
        {'label': 'Vicki Zhao Wei', 'value': 'Vicki_Zhao_Wei.csv'}
    ],
    value='LeBron_James.csv',id = 'subject_options'
)], id='subject'),

    # creates divs for images
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

# slider
], id='main_wrapper'),
    html.Div([
        dcc.Slider(
        id='threshold-slider',
        min=-0.0,
        value = 0.0
    )]),

    html.Div(
     id='slider-output-container', className = 'slider'
    ),

    html.Div(
     html.H3('Resources')
    )
])

#loads all images and slider with current subject
@app.callback([Output('celeb', 'src'), Output('img1', 'src'), Output('img2', 'src'), Output('img3', 'src'), Output('img4', 'src'), Output('img5', 'src'),
Output('img6', 'src'), Output('img7', 'src'), Output('img8', 'src'), Output('img9', 'src'), Output('img10', 'src'), Output('threshold-slider', 'max'), Output('threshold-slider', 'step'),
Output('threshold-slider', 'marks'), Output('current_data_similarity', 'children'), Output('current_data_names', 'children'), Output('current_match_values', 'children'), Output('threshold-slider', 'value')], [Input('subject_options', 'value')])
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

    #download match booleans
    matches = results['Match']

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
        step, steps, similarity, names, matches, 0.0]

# threshold image 1
@app.callback([Output('img1', 'style'), Output('name1', 'children'), Output('sim1', 'children')],
    [Input('threshold-slider', 'value'), Input('current_data_similarity', 'children'), Input('current_data_names', 'children'), Input('current_match_values', 'children')])
def update_output(threshold, similarity, names, match):
    if similarity[0] >= threshold:
        if match[0]:
            return {"border":"10px green solid"}, names[0], str(round(similarity[0], 3))
        else:
            return {"border":"10px yellow solid"}, names[0], str(round(similarity[0], 3))
    else:
        return {"border":"10px black solid"}, names[0], str(round(similarity[0], 3))

#threshold image 2
@app.callback([Output('img2', 'style'),Output('name2', 'children'), Output('sim2', 'children')],
    [Input('threshold-slider', 'value'), Input('current_data_similarity', 'children'), Input('current_data_names', 'children'), Input('current_match_values', 'children')])
def update_output(threshold, similarity, names, match):
    if similarity[1] >= threshold:
        if match[1]:
            return {"border":"10px green solid"}, names[1], str(round(similarity[1], 3))
        else:
            return {"border":"10px yellow solid"}, names[1], str(round(similarity[1], 3))
    else:
        return {"border":"10px black solid"}, names[1], str(round(similarity[1], 3))

#threshold image 3
@app.callback([Output('img3', 'style'),Output('name3', 'children'), Output('sim3', 'children')],
    [Input('threshold-slider', 'value'), Input('current_data_similarity', 'children'), Input('current_data_names', 'children'), Input('current_match_values', 'children')])
def update_output(threshold, similarity, names, match):
    if similarity[2] >= threshold:
        if match[2]:
            return {"border":"10px green solid"}, names[2], str(round(similarity[2], 3))
        else:
            return {"border":"10px yellow solid"}, names[2], str(round(similarity[2], 3))
    else:
        return {"border":"10px black solid"}, names[2], str(round(similarity[2], 3))

#threshold image 4
@app.callback([Output('img4', 'style'),Output('name4', 'children'), Output('sim4', 'children')],
    [Input('threshold-slider', 'value'), Input('current_data_similarity', 'children'), Input('current_data_names', 'children'), Input('current_match_values', 'children')])
def update_output(threshold, similarity, names, match):
    if similarity[3] >= threshold:
        if match[3]:
            return {"border":"10px green solid"}, names[3], str(round(similarity[3], 3))
        else:
            return {"border":"10px yellow solid"}, names[3], str(round(similarity[3], 3))
    else:
        return {"border":"10px black solid"}, names[3], str(round(similarity[3], 3))

#threshold image 5
@app.callback([Output('img5', 'style'),Output('name5', 'children'), Output('sim5', 'children')],
    [Input('threshold-slider', 'value'), Input('current_data_similarity', 'children'), Input('current_data_names', 'children'), Input('current_match_values', 'children')])
def update_output(threshold, similarity, names, match):
    if similarity[4] >= threshold:
        if match[4]:
            return {"border":"10px green solid"}, names[4], str(round(similarity[4], 3))
        else:
            return {"border":"10px yellow solid"}, names[4], str(round(similarity[4], 3))
    else:
        return {"border":"10px black solid"}, names[4], str(round(similarity[4], 3))

#threshold image 6
@app.callback([Output('img6', 'style'),Output('name6', 'children'), Output('sim6','children')],
    [Input('threshold-slider', 'value'), Input('current_data_similarity', 'children'), Input('current_data_names', 'children'), Input('current_match_values', 'children')])
def update_output(threshold, similarity, names, match):
    if similarity[5] >= threshold:
        if match[5]:
            return {"border":"10px green solid"}, names[5], str(round(similarity[5], 3))
        else:
            return {"border":"10px yellow solid"}, names[5], str(round(similarity[5], 3))
    else:
        return {"border":"10px black solid"}, names[5], str(round(similarity[5], 3))

#threshold image 7
@app.callback([Output('img7', 'style'),Output('name7', 'children'), Output('sim7', 'children')],
    [Input('threshold-slider', 'value'), Input('current_data_similarity', 'children'), Input('current_data_names', 'children'), Input('current_match_values', 'children')])
def update_output(threshold, similarity, names, match):
    if similarity[6] >= threshold:
        if match[6]:
            return {"border":"10px green solid"}, names[6], str(round(similarity[6], 3))
        else:
            return {"border":"10px yellow solid"}, names[6], str(round(similarity[6], 3))
    else:
        return {"border":"10px black solid"}, names[6], str(round(similarity[6], 3))

#threshold image 8
@app.callback([Output('img8', 'style'),Output('name8', 'children'), Output('sim8', 'children')],
    [Input('threshold-slider', 'value'), Input('current_data_similarity', 'children'), Input('current_data_names', 'children'), Input('current_match_values', 'children')])
def update_output(threshold, similarity, names, match):
    if similarity[7] >= threshold:
        if match[7]:
            return {"border":"10px green solid"}, names[7], str(round(similarity[7], 3))
        else:
            return {"border":"10px yellow solid"}, names[7], str(round(similarity[7], 3))
    else:
        return {"border":"10px black solid"}, names[7], str(round(similarity[7], 3))

#threshold image 9
@app.callback([Output('img9', 'style'),Output('name9', 'children'), Output('sim9', 'children')],
    [Input('threshold-slider', 'value'), Input('current_data_similarity', 'children'), Input('current_data_names', 'children'), Input('current_match_values', 'children')])
def update_output(threshold, similarity, names, match):
    if similarity[8] >= threshold:
        if match[8]:
            return {"border":"10px green solid"}, names[8], str(round(similarity[8], 3))
        else:
            return {"border":"10px yellow solid"}, names[8], str(round(similarity[8], 3))
    else:
        return {"border":"10px black solid"}, names[8], str(round(similarity[8], 3))

#threshold image 10
@app.callback([Output('img10', 'style'),Output('name10', 'children'), Output('sim10', 'children')],
    [Input('threshold-slider', 'value'), Input('current_data_similarity', 'children'), Input('current_data_names', 'children'), Input('current_match_values', 'children')])
def update_output(threshold, similarity, names, match):
    if similarity[9] >= threshold:
        if match[9]:
            return {"border":"10px green solid"}, names[9], str(round(similarity[9], 3))
        else:
            return {"border":"10px yellow solid"}, names[9], str(round(similarity[9], 3))
    else:
        return {"border":"10px black solid"}, names[9], str(round(similarity[9], 3))

# threshold text
@app.callback(
    dash.dependencies.Output('slider-output-container', 'children'),
    [dash.dependencies.Input('threshold-slider', 'value')])
def update_output(value):
    return 'Threshold: You have selected a minimum similiarity score to qualify for a match as "{}"'.format(value)

# @app.callback(
#     dash.dependencies.Output('subject', 'children'),
#     [dash.dependencies.Input('celeb', 'n_clicks')])
# def update_output(clicks):
#     if clicks != None:
#         return 'Clicked!'



if __name__ == '__main__':
    app.run_server(debug=True)
