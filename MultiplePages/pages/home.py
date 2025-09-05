import dash 
from dash import html 

##ONLY RUN FROM app.py**
dash.register_page(__name__, path = "/")

#only want one app that has all pages because have app already in another file here 
layout = html.Div([
    html.H2("Welcome to my HomePage"), 
    html.P("This is a simple multipage Dash project")
    
])
