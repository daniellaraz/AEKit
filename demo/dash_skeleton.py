import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import pandas as pd
import plotly.graph_objs as go
import math
import os
import logging


app = dash.Dash(__name__)
app.title = 'Facial Recognition Demo'
server = app.server


# introduction text
app.layout = html.Div([
    html.Div([
        html.H2("Facial Recognition Demo", id='title', style={'font-family': 'Monaco'}),
        # purpose section
        html.Div([
            html.H3("Purpose: ", id = 'purpose', style = {'font-weight': 'bold', 'font-family': 'Monaco'}),
            html.P("The goal of this demo is to highlight some of the harms of facial recognition systems. Though there are many issues with facial recognition software, this tool demonstrates two in particular. "),
            html.Span("First, ", style={'font-weight': 'bold'}),
            "we illustrate how facial recognition software relies on thresholds, which are often arbitrarily set, to determine whether two faces in a photo are a match. ",
            "At its simplest, two images are compared and given a numerical value on a continuous scale that represents how similar the images are. ",
            "A cut-off value is selected, meaning that any similarity score greater than that cut-off value will be considered a match, and anything below or equal to that value is not considered a match. ",
            "But, what decides this cut-off value? ",
                ]),
        html.Div([
             html.Span("Second, ", style={"font-weight": "bold"}), 
             " we demonstrate, as has been shown in academic and policy literature, that facial recognition software misidentifies people of color, specifically women of color, more often than it does white people. Yet, facial recognition is frequently used to police black and brown communities - the very people the software identifies most poorly.", 
            ]),
        # terms to know section
        html.Div([
            html.H3("Terms to Know: ", id = "terms", style = {'font-weight': 'bold', 'font-family': 'Monaco'}),
            html.P("The following are some helpful terms for better understanding this demo."),
            html.Span("Similarity Score: ", style={'font-weight': 'bold'}),
            " a value ",
            "    ",
                ]),
        html.Div([
             html.Span("False Positive: ", style={"font-weight": "bold"}), 
             "occurs when images that are not of the same person are incorrectly labeled as a match because their similarity score exceeded the minimum required to be considered a match.", 
            ]),
        html.Div([
             html.Span("True Positive: ", style={"font-weight": "bold"}), 
             "occurs when two images, which are indeed of the same person, are correctly labeled as a match. ", 
            "In our demo, true positives are outlined in ",
             html.Span('green', style={'background-color': '#A6CA45', 'font-weight': 'bold'}),
            ]),    

        # instructions section
        html.H3('Instructions:', id='instructions', style={'font-family': 'Monaco'}),        
        html.P("1. Enter full screen in your browser. You'll see the demo has 3 main sections - 'Current Subject, 'Matches', and 'Threshold'. "),
        html.Div([
            "2. Under 'Matches' you'll see those faces that have matched with the face under 'Current Subject'. Below each match is the similarity score between the 'Current Subject' and that match. For ease of interpretation, in this demo the larger the similarity score, the more similar two images are. The only true positive match is that which is outlined in green. All other matches are false positives.",
                ]),
        html.P("3. In the 'Threshold' section you'll see a slider. Move the slider by clicking on the numbered intervals. This changes the minimum similarity score required in order to be considered a match. As you move the slider, you'll see some matches fade away as their similarity score exceeds the minimum threshold you've set. "),
        html.P("4. Under 'Current Subject', you'll see a list of other options. Click through the diverse list of celebrities, playing around with the threshold slider as well. Take note of how effecitvely, or ineffectively, the software identifies true matches. "),
            ]),


        # questions to consider section
        html.Div([
            html.H3("Questions to Consider: ", id = "questions", style = {'font-weight': 'bold', 'font-family': 'Monaco'}),
            html.P("While you use this demo, consider the following questions."),
            html.P("1. Compare similarity scores and thresholds across 'Current Subjects' of different races and ethnicities. What is the lowest threshold at which the software correctly identifies Aaron Piersol's face among the potential matches? What is the lowest threshold at which the software correctly identifies LeBron James' face among the potential matches? Finally, what is the lowest threshold at which the software correctly identifies Jacqueline Edwards' face among the potential matches?"),
            html.P("2. Consider whether making facial recognition software more accurate for people of color would actually make the technology safe to use. More accurate facial recognition software that better identifies faces could contribute to policing and surveillance of communities of color, undocumented immigrants, and others. Does such a software have a place in our society?")
                ]),



    # stores current subject data
    html.Div([ html.Div(id='current_data_similarity', style={'display': 'none'}, children=[0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0]),
    html.Div(id='current_data_names', style={'display': 'none'}, children=['','','','','','','','']),
    html.Div(id='current_match_values', style={'display': 'none'}, children=[False,False,False,False,False,False,False,False]),

#    subject and radio button options to switch subject 
    html.Div([
        html.H4('Current Subject:'),
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
    value='LeBron_James.csv',
    labelStyle={'display': 'inline-block'},
    id = 'subject_options'
)], id='subject'),




    # creates divs for images
    html.Div([
        html.H4('Current Matches:'),
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
     ": In 2017, the Washington County Police Department in Oregon pioneered the use of Amazon's facial recognition software tool, Rekognition, to compare surveillance footage of people's faces to a database of mug shot photos to identify burglary suspects. Oregon Live reports that deputies are permitted to run artist sketches into the search. As our demo illustrates, the use of facial recognition software often results in false positives, putting innocent people at risk for being targeted and arrested. Since the software is less accurate on people of color, this community faces a heightened risk of being targeted by law enforcement. The similarity threshold that the police department uses impacts their rate of false positives. Although Amazon recommends only using its Rekognition tool with a 99% similarity threshold to identify suspects for law enforcement purposes, police departments are not required to follow these guidelines. ",
     dcc.Link('Washington Post Coverage featured in Oregon Live, ', href='https://www.oregonlive.com/washingtoncounty/2019/05/amazons-facial-recognition-technology-is-supercharging-washington-county-police.html'),
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
    print("updating output: ", value)
    #data = load_data(value)
    results = pd.read_csv(value)
    print("updated value: ", value)
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
            return {"border":"10px white solid"}, names[0], str(round(similarity[0], 3))
    else:
        return {"border":"10px white solid", "opacity": "0.2"}, names[0], str(round(similarity[0], 3))

#threshold image 2
@app.callback([Output('img2', 'style'),Output('name2', 'children'), Output('sim2', 'children')],
    [Input('threshold-slider', 'value'), Input('current_data_similarity', 'children'), Input('current_data_names', 'children'), Input('current_match_values', 'children')])
def update_output(threshold, similarity, names, match):
    if similarity[1] >= threshold:
        if match[1]:
            return {"border":"10px #A6CA45 solid"}, names[1], str(round(similarity[1], 3))
        else:
            return {"border":"10px white solid"}, names[1], str(round(similarity[1], 3))
    else:
        return {"border":"10px white solid", "opacity": "0.2"}, names[1], str(round(similarity[1], 3))

#threshold image 3
@app.callback([Output('img3', 'style'),Output('name3', 'children'), Output('sim3', 'children')],
    [Input('threshold-slider', 'value'), Input('current_data_similarity', 'children'), Input('current_data_names', 'children'), Input('current_match_values', 'children')])
def update_output(threshold, similarity, names, match):
    if similarity[2] >= threshold:
        if match[2]:
            return {"border":"10px #A6CA45 solid"}, names[2], str(round(similarity[2], 3))
        else:
            return {"border":"10px white solid"}, names[2], str(round(similarity[2], 3))
    else:
        return {"border":"10px white solid", "opacity": "0.2"}, names[2], str(round(similarity[2], 3))

#threshold image 4
@app.callback([Output('img4', 'style'),Output('name4', 'children'), Output('sim4', 'children')],
    [Input('threshold-slider', 'value'), Input('current_data_similarity', 'children'), Input('current_data_names', 'children'), Input('current_match_values', 'children')])
def update_output(threshold, similarity, names, match):
    if similarity[3] >= threshold:
        if match[3]:
            return {"border":"10px #A6CA45 solid"}, names[3], str(round(similarity[3], 3))
        else:
            return {"border":"10px white solid"}, names[3], str(round(similarity[3], 3))
    else:
        return {"border":"10px white solid", "opacity": "0.2"}, names[3], str(round(similarity[3], 3))

#threshold image 5
@app.callback([Output('img5', 'style'),Output('name5', 'children'), Output('sim5', 'children')],
    [Input('threshold-slider', 'value'), Input('current_data_similarity', 'children'), Input('current_data_names', 'children'), Input('current_match_values', 'children')])
def update_output(threshold, similarity, names, match):
    if similarity[4] >= threshold:
        if match[4]:
            return {"border":"10px #A6CA45 solid"}, names[4], str(round(similarity[4], 3))
        else:
            return {"border":"10px white solid"}, names[4], str(round(similarity[4], 3))
    else:
        return {"border":"10px white solid", "opacity": "0.2"}, names[4], str(round(similarity[4], 3))

#threshold image 6
@app.callback([Output('img6', 'style'),Output('name6', 'children'), Output('sim6','children')],
    [Input('threshold-slider', 'value'), Input('current_data_similarity', 'children'), 
    Input('current_data_names', 'children'), Input('current_match_values', 'children')])
def update_output(threshold, similarity, names, match):
    if similarity[5] >= threshold:
        if match[5]:
            return {"border":"10px #A6CA45 solid"}, names[5], str(round(similarity[5], 3))
        else:
            return {"border":"10px white solid"}, names[5], str(round(similarity[5], 3))
    else:
        return {"border":"10px white solid", "opacity": "0.2"}, names[5], str(round(similarity[5], 3))

#threshold image 7
@app.callback([Output('img7', 'style'),Output('name7', 'children'), Output('sim7', 'children')],
    [Input('threshold-slider', 'value'), Input('current_data_similarity', 'children'), Input('current_data_names', 'children'), Input('current_match_values', 'children')])
def update_output(threshold, similarity, names, match):
    if similarity[6] >= threshold:
        if match[6]:
            return {"border":"10px #A6CA45 solid"}, names[6], str(round(similarity[6], 3))
        else:
            return {"border":"10px white solid"}, names[6], str(round(similarity[6], 3))
    else:
        return {"border":"10px white solid", "opacity": "0.2"}, names[6], str(round(similarity[6], 3))

#threshold image 8
@app.callback([Output('img8', 'style'),Output('name8', 'children'), Output('sim8', 'children')],
    [Input('threshold-slider', 'value'), Input('current_data_similarity', 'children'), Input('current_data_names', 'children'), Input('current_match_values', 'children')])
def update_output(threshold, similarity, names, match):
    if similarity[7] >= threshold:
        if match[7]:
            return {"border":"10px #A6CA45 solid"}, names[7], str(round(similarity[7], 3))
        else:
            return {"border":"10px white solid"}, names[7], str(round(similarity[7], 3))
    else:
        return {"border":"10px black solid", "opacity": "0.2"}, names[7], str(round(similarity[7], 3))

# threshold text
@app.callback(
    dash.dependencies.Output('slider-output-container', 'children'),
    [dash.dependencies.Input('threshold-slider', 'value')])
def update_output(value):
    return 'Threshold: You have selected a minimum similarity score to qualify for a match as "{}"'.format(value)


if __name__ == '__main__':
    port = os.environ.get('PORT') or 8035
   # debug = 'DYNO' not in os.environ
    app.run_server(port=port, debug=debug)
