import dash 
from dash import html 

##ONLY RUN FROM app.py**
dash.register_page(__name__, path = "/page1", name = "Page 1")

layout = html.Div([
    html.H2("Page 1", className = "page-title"),
    ##TopRow
    html.Div("Top Row: with 1 Column", className = "block block-top"), 
    
    ##Middle 2 column
    html.Div([
        html.Div("Middle Left", className = "block"),
        html.Div("Middle Right", className = "block")
    ], className = "row-2"), #styles the entire row
    
    ##Footer 
    html.Div("Footer", className = "block block-footer")
    
], className = "page1-grid")