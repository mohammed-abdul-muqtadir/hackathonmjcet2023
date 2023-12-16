import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import pandas as pd
import dash_bootstrap_components as dbc

# Sample data
months = list(range(1, 13))
loan_data = pd.DataFrame({
    'Months': months,
    'Loan_Amount': [1000, 1500, 2000, 2500, 3000, 3500, 4000, 4500, 5000, 5500, 6000, 6500],
})

# Initialize the Dash app
def loan_vis(flask_app):
    app = dash.Dash(server=flask_app,name="loan",url_base_pathname="/loan/")

    # Layout of the app
    app.layout = html.Div([
        html.H1("Loan vs Months"),
        dcc.Graph(id='loan-graph'),

        html.Div([
            html.Label("Percentage"),
            dcc.Slider(
                id='percentage-slider',
                min=0,
                max=100,
                step=1,
                marks={i: f'{i}%' for i in range(0, 101, 10)},
                value=50
            ),

            html.Label("Months"),
            dcc.Slider(
                id='months-slider',
                min=1,
                max=12,
                marks={i: str(i) for i in range(1, 13)},
                value=6
            ),

            html.Label("Loan Amount (₹)"),  # Changed from "$" to "₹"
            dcc.Slider(
                id='loan-amount-slider',
                min=1,
                max=100000,
                step=5000,
                marks={i * 5000: f'₹{i * 5000}' for i in range(21)},  # Adjusted the range and step
                value=25000
            ),
        ], style={'margin': '20px'})
    ])


    # Callback to update the graph based on slider values
    @app.callback(
        Output('loan-graph', 'figure'),
        [Input('percentage-slider', 'value'),
         Input('months-slider', 'value'),
         Input('loan-amount-slider', 'value')]
    )
    def update_graph(percentage, months, loan_amount):
        # Calculate loan data based on sliders
        loan_data['Loan'] = loan_amount * (1 + percentage / 100) ** (loan_data['Months'] / months)

        # Plotly figure
        fig = {
            'data': [
                {'x': loan_data['Months'], 'y': loan_data['Loan'], 'type': 'line', 'name': 'Loan'},
            ],
            'layout': {
                'title': f'Loan vs Months (Percentage: {percentage}%, Months: {months}, Loan Amount: ₹{loan_amount})',
                'xaxis': {'title': 'Months'},
                'yaxis': {'title': 'Loan Amount (₹)'},
            }
        }

        return fig


# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)
