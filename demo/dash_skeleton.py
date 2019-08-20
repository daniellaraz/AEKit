import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import pandas as pd
import plotly.graph_objs as go
import math


app = dash.Dash(__name__)
app.title = 'Facial Recognition Demo'


# introduction text
app.layout = html.Div([
    html.Div([
        html.H2('Facial Recognition Demo', id='title'),
        html.Div([
        html.Span('Purpose: ', style = {'font-weight': 'bold'}),
        'The goal of this demo is to explain the process of determining matches using facial recognition technology based on setting a minimum similarity score (',
        html.Span('threshold), ', style = {"font-weight": 'bold'}),
        html.Span('false positives, ', style = {'font-weight': 'bold'}),
        "facial recognition's bias against people, especially women, of color, and the philosophical problems with employing facial recognition systems, regardless of accuracy rates."
        ]),
        html.H4('Instructions:', id='instructions'),
        html.P("1. Enter full screen in your browser. Listed below each celebrity name is the similarity score that resulted from comparing that image to the current subject using an open source facial recognition system."),
        html.Div([
    "2. Move the slider by clicking on the number intervals to change the minimum similarity required between the celebrity subject and each image to qualify as a match, which we refer to as the",
    html.Span(" threshold. ", style = {"font-weight": "bold"}),
    "The larger the similarity score is, the more similar two images are. We refer to images that match according to the similarity threshold, but aren't really the same person, as ",
    html.Span('false positives. False positives ', style={'font-weight': 'bold'}),
    'are outlined in ',
    html.Span('red', style={'background-color': '#D34640', 'font-weight': 'bold'}),
    '. When the images match and are truly the same person, we call this a  ',
    html.Span('true positive. True positives ', style={'font-weight': 'bold'}),
    'are outlined in ',
    html.Span('green', style={'background-color': '#A6CA45', 'font-weight': 'bold'}),
    ". We refer to images with similarity scores that fall below the threshold and don't match as ",
    html.Span('non-matches. Non-matches ', style={'font-weight': 'bold'}),
    'fade and are outlined in ',
    html.Span('black.', style={'font-weight': 'bold'})
]),
        html.P("3. Notice differences in similarity scores of the 8 images for subjects of different skin tones and genders. Research shows facial recognition software to have lower accuracy for people, especially women, of color. For instance, notice how when Jacqueline Edwards is the subject, Kelly White has a higher similarity score to Jacqueline Edwards than a different picture of Jacqueline Edwards to herself."),
        html.P("4. Analyze a different subject by choosing from the subject options on the left side of the demo."),
        html.P("5. Consider that making facial recognition technology  more accurate for people, especially women, of color would not make the technology safe for use. Washington State Activist Maru Mora-Villalpando explains that facial recognition exacerbates the policing of black and brown communities, and more accurate facial recognition technology would only contribute to this issue. Speaking specifically on the use of facial recognition technology to target undocumented immigrants, Mora-Villalpando emphasizes, 'We believe that Amazon is harming our communities if they continue with their push of selling this software [facial recognition] to ICE.'")

     ]),

    # stores current subject data
    html.Div([ html.Div(id='current_data_similarity', style={'display': 'none'}, children=[0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0]),
    html.Div(id='current_data_names', style={'display': 'none'}, children=['','','','','','','','']),
    html.Div(id='current_match_values', style={'display': 'none'}, children=[False,False,False,False,False,False,False,False]),

    # subject and radio button options to switch subject
    html.Div([
        html.H4('Current subject'),
        html.Img(id='celeb'), dcc.RadioItems(
    options=[
        {'label': 'LeBron James', 'value': 'LeBron_James.csv'},
        {'label': 'Lisa Leslie', 'value': 'Lisa_Leslie.csv'},
        {'label': 'Paris Hilton', 'value': 'Paris_Hilton.csv'},
        {'label': 'Jennifer Lopez', 'value': 'Jennifer_Lopez.csv'},
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
            ],
            className = 'box'),

# slider

    html.Div([
        dcc.Slider(
        id='threshold-slider',
        min=-0.0,
        value = 0.0
    ), html.Div(
     id='slider-output-container', className = 'slider'
    )], id = 'slider')], id = "interactive"),

    html.Div([
     html.H3('Case Studies:'),
     html.Div([

     html.Span("ICE Uses Facial Recognition To Sift State Driver's License Record", style = {'font-weight': 'bold'}),
     ": In July of 2019, researchers at Georgetown University Law Center found that Immigration and Customs Enforcement (ICE) agents mined millions of driver license photographs in search of facial recognition matches to target undocumented migrants who have legally obtained driver licenses. ICE did this illegally, as they did not have congressional approval to access DMV databases of driver license photos. In this scenario, the use of facial recognition technology clearly put undocumented migrants at risk, and increased accuracy of the facial recognition software would have heightened the danger towards undocumented migrants. Not only does facial recognition software work less well on people of color, even if it is accurate, it's used to target communities of color. ",
     dcc.Link('Read the NPR news coverage of this case study here.', href='https://www.npr.org/2019/07/08/739491857/ice-uses-facial-recognition-to-sift-state-drivers-license-records-researchers-sa'),
     ]),
     html.H4(' '),
     html.Span('Washington County Police Department', style = {'font-weight': 'bold'}),
     ": In 2017, the Washington County Police Department in Oregon pionee#D34640 the use of Amazon's facial recognition software tool, Rekognition, to compare surveillance footage of people's faces to a database of mug shot photos to identify burglary suspects. Oregon Live reports that deputies are permitted to run artist sketches into the search. As our demo illustrates, the use of facial recognition software often results in false positives, putting innocent people at risk for being targeted and arrested. Since the software is less accurate on people of color, this community faces a heightened risk of being targeted by law enforcement. The similarity threshold that the police department uses impacts their rate of false positives. Although Amazon recommends only using its Rekognition tool with a 99% similarity threshold to identify suspects for law enforcement purposes, police departments are not requi#D34640 to follow these guidelines. ",
     dcc.Link('Washington Post Coverage featu#D34640 in Oregon Live, ', href='https://www.oregonlive.com/washingtoncounty/2019/05/amazons-facial-recognition-technology-is-supercharging-washington-county-police.html'),
     dcc.Link('KGW  Portland Coverage, ', href='https://www.kgw.com/article/money/aclu-calls-out-amazon-washington-co-sheriffs-office-for-facial-recognition-tech/283-557099068'),
     dcc.Link('Official Amazon guidelines', href = 'https://docs.aws.amazon.com/rekognition/latest/dg/collections.html')


    ], id = "case_studies"),

    html.Div([
     html.H3('Resources:'),
     html.Div([
     html.Span("Facial Recognition Model", style = {'font-weight': 'bold'}),
     ": We used Open Face's Open Source Facial Recognition model to run our images and determine matches. We ran Open Face's model using a Docker container. We edited Open Face's image comparison Python file to only compare one specified image against the entire dataset of images, instead of each image in the dataset to every other image.",
     html.H4(' '),
     html.Span("Images", style = {'font-weight': 'bold'}),
     ": We obtained nearly all our images from Labeled Faces in the Wild, an  open dataset of celebrity photos. For celebrity subjects who did not have more than one photo in the Labeled Faces in the Wild dataset, we supplemented with images from Google Image searches."
     ]),
    ], id = "resources")
])

#loads all images and slider with current subject
@app.callback([Output('celeb', 'src'), Output('img1', 'src'), Output('img2', 'src'), Output('img3', 'src'), Output('img4', 'src'), Output('img5', 'src'),
Output('img6', 'src'), Output('img7', 'src'), Output('img8', 'src'), Output('threshold-slider', 'max'), Output('threshold-slider', 'step'),
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
        images[5], images[6], images[7], threshold_upper,
        step, steps, similarity, names, matches, 0.0]

# threshold image 1
@app.callback([Output('img1', 'style'), Output('name1', 'children'), Output('sim1', 'children')],
    [Input('threshold-slider', 'value'), Input('current_data_similarity', 'children'), Input('current_data_names', 'children'), Input('current_match_values', 'children')])
def update_output(threshold, similarity, names, match):
    if similarity[0] >= threshold:
        if match[0]:
            return {"border":"10px #A6CA45 solid"}, names[0], str(round(similarity[0], 3))
        else:
            return {"border":"10px #D34640 solid"}, names[0], str(round(similarity[0], 3))
    else:
        return {"border":"10px black solid", "opacity": "0.2"}, names[0], str(round(similarity[0], 3))

#threshold image 2
@app.callback([Output('img2', 'style'),Output('name2', 'children'), Output('sim2', 'children')],
    [Input('threshold-slider', 'value'), Input('current_data_similarity', 'children'), Input('current_data_names', 'children'), Input('current_match_values', 'children')])
def update_output(threshold, similarity, names, match):
    if similarity[1] >= threshold:
        if match[1]:
            return {"border":"10px #A6CA45 solid"}, names[1], str(round(similarity[1], 3))
        else:
            return {"border":"10px #D34640 solid"}, names[1], str(round(similarity[1], 3))
    else:
        return {"border":"10px black solid", "opacity": "0.2"}, names[1], str(round(similarity[1], 3))

#threshold image 3
@app.callback([Output('img3', 'style'),Output('name3', 'children'), Output('sim3', 'children')],
    [Input('threshold-slider', 'value'), Input('current_data_similarity', 'children'), Input('current_data_names', 'children'), Input('current_match_values', 'children')])
def update_output(threshold, similarity, names, match):
    if similarity[2] >= threshold:
        if match[2]:
            return {"border":"10px #A6CA45 solid"}, names[2], str(round(similarity[2], 3))
        else:
            return {"border":"10px #D34640 solid"}, names[2], str(round(similarity[2], 3))
    else:
        return {"border":"10px black solid", "opacity": "0.2"}, names[2], str(round(similarity[2], 3))

#threshold image 4
@app.callback([Output('img4', 'style'),Output('name4', 'children'), Output('sim4', 'children')],
    [Input('threshold-slider', 'value'), Input('current_data_similarity', 'children'), Input('current_data_names', 'children'), Input('current_match_values', 'children')])
def update_output(threshold, similarity, names, match):
    if similarity[3] >= threshold:
        if match[3]:
            return {"border":"10px #A6CA45 solid"}, names[3], str(round(similarity[3], 3))
        else:
            return {"border":"10px #D34640 solid"}, names[3], str(round(similarity[3], 3))
    else:
        return {"border":"10px black solid", "opacity": "0.2"}, names[3], str(round(similarity[3], 3))

#threshold image 5
@app.callback([Output('img5', 'style'),Output('name5', 'children'), Output('sim5', 'children')],
    [Input('threshold-slider', 'value'), Input('current_data_similarity', 'children'), Input('current_data_names', 'children'), Input('current_match_values', 'children')])
def update_output(threshold, similarity, names, match):
    if similarity[4] >= threshold:
        if match[4]:
            return {"border":"10px #A6CA45 solid"}, names[4], str(round(similarity[4], 3))
        else:
            return {"border":"10px #D34640 solid"}, names[4], str(round(similarity[4], 3))
    else:
        return {"border":"10px black solid", "opacity": "0.2"}, names[4], str(round(similarity[4], 3))

#threshold image 6
@app.callback([Output('img6', 'style'),Output('name6', 'children'), Output('sim6','children')],
    [Input('threshold-slider', 'value'), Input('current_data_similarity', 'children'), Input('current_data_names', 'children'), Input('current_match_values', 'children')])
def update_output(threshold, similarity, names, match):
    if similarity[5] >= threshold:
        if match[5]:
            return {"border":"10px #A6CA45 solid"}, names[5], str(round(similarity[5], 3))
        else:
            return {"border":"10px #D34640 solid"}, names[5], str(round(similarity[5], 3))
    else:
        return {"border":"10px black solid", "opacity": "0.2"}, names[5], str(round(similarity[5], 3))

#threshold image 7
@app.callback([Output('img7', 'style'),Output('name7', 'children'), Output('sim7', 'children')],
    [Input('threshold-slider', 'value'), Input('current_data_similarity', 'children'), Input('current_data_names', 'children'), Input('current_match_values', 'children')])
def update_output(threshold, similarity, names, match):
    if similarity[6] >= threshold:
        if match[6]:
            return {"border":"10px #A6CA45 solid"}, names[6], str(round(similarity[6], 3))
        else:
            return {"border":"10px #D34640 solid"}, names[6], str(round(similarity[6], 3))
    else:
        return {"border":"10px black solid", "opacity": "0.2"}, names[6], str(round(similarity[6], 3))

#threshold image 8
@app.callback([Output('img8', 'style'),Output('name8', 'children'), Output('sim8', 'children')],
    [Input('threshold-slider', 'value'), Input('current_data_similarity', 'children'), Input('current_data_names', 'children'), Input('current_match_values', 'children')])
def update_output(threshold, similarity, names, match):
    if similarity[7] >= threshold:
        if match[7]:
            return {"border":"10px #A6CA45 solid"}, names[7], str(round(similarity[7], 3))
        else:
            return {"border":"10px #D34640 solid"}, names[7], str(round(similarity[7], 3))
    else:
        return {"border":"10px black solid", "opacity": "0.2"}, names[7], str(round(similarity[7], 3))

# threshold text
@app.callback(
    dash.dependencies.Output('slider-output-container', 'children'),
    [dash.dependencies.Input('threshold-slider', 'value')])
def update_output(value):
    return 'Threshold: You have selected a minimum similarity score to qualify for a match as "{}"'.format(value)


if __name__ == '__main__':
    app.run_server(debug=True)
