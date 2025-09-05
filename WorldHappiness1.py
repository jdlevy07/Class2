from dash import Dash, html
import pandas as pd 
import plotly.express as px 

#load dataset 
df = pd.read_csv

app = Dash(__name__)

app.layout = html.Div([
    html.H1("World Happiness Dashboard"),
    html.P("This dashboard visualizes world happiness scores."),
    html.Br(),
    html.A("World Happiness Report", href = 'https://worldhappiness.report/', target = "_blank",
           style = {"color":"#6065a3", "textDecoration": "underline"})
    
    
])

if __name__ == "__main__":
    app.run(debug=True)
    
    