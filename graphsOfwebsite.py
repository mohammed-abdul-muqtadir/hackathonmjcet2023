import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px
import dash_bootstrap_components as dbc
from dash_bootstrap_templates import load_figure_template
def create_dash_application(flask_app):
    app = dash.Dash(external_stylesheets=[dbc.themes.CYBORG],server=flask_app,name="dashboard",url_base_pathname="/dash/")

# Data for bar charts
    income = {"income": ["active income", "passive income"],
              "value": [10, 12]}
    assets = {'Category': ["stock", "bond", "commodities"],
              'Value': [30, 20, 50]}

# Data for pie charts
    pie_data = {'Label': ["assets", "liabilities"],
                'Value': [40, 30]}
    loan = {"debt": ["hdfc", "sbi", "icici"],
            "value": [10, 20, 20]}

# Layout of the app
    app.layout = html.Div([
        html.Header(html.H1("User Dashboard")),
        html.Div([
            dcc.Graph(
                id='bar-chart',
                figure=px.bar(income, x='value', y='income', title='Horizontal Bar Chart', orientation="h")
            )
        ], style={"height": "30%",'width': '50%', 'display': 'inline-block'}),

        html.Div([
            dcc.Graph(
                id='pie-chart',
                figure=px.pie(pie_data, values='Value', names='Label', title='Pie Chart')
            )
        ], style={"height": "30%",'width': '50%', 'display': 'inline-block', 'float': 'right'}),

        html.Div([
            dcc.Graph(
                id='horizontal-bar-chart',
                figure=px.bar(assets, x='Value', y='Category', title='Horizontal Bar Chart', orientation="h")
            )
        ], style={"height": "30%",'width': '50%', 'display': 'inline-block'}),

        html.Div([
            dcc.Graph(
                id='pie-chart-2',
                figure=px.pie(loan, values='value', names='debt', title='Pie Chart')
            )
        ], style={"height": "30%",'width': '50%', 'display': 'inline-block', 'float': 'right'}),
    ])

if __name__ == '__main__':
    app.run_server(debug=True)
