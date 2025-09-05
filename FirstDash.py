##import my dash library 
from dash import Dash, html

##create my dash app
app = Dash(__name__)
app.title = "My First Dash App" #goes in the tab on webpage 

##Define the layout 
app.layout = html.Div([
    html.H1("Hello Dash", style={'color': "#9A77C8",
                                 'font': '20px',
                                 'backgroundColor': "#A598E8"}), #first header
    html.P("This is a simple dashboard", style = {'border': '1px solid black',
                                                  'padding':'20px',
                                                  'margin':'50px'}), #paragraph
    html.Br(), #line break 
    html.A("Click here", href="https://example.com") #add link 
])

##run the app 
if __name__ == "__main__":
    app.run(debug=True, use_reloader=False)