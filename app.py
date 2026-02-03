import dash
from dash import dcc, html
import pandas as pd
import plotly.express as px

# Read the formatted data
df = pd.read_csv('formatted_data.csv')

# Convert date to datetime and sort
df['date'] = pd.to_datetime(df['date'])
df = df.sort_values('date')

# Group by date to get total sales per day
daily_sales = df.groupby('date')['sales'].sum().reset_index()

# Create the line chart
fig = px.line(
    daily_sales,
    x='date',
    y='sales',
    title='Pink Morsels Daily Sales Over Time',
    labels={
        'date': 'Date',
        'sales': 'Sales ($)'
    },
    markers=True
)

# Customize the chart
fig.update_layout(
    xaxis_title='Date',
    yaxis_title='Sales ($)',
    hovermode='x unified'
)

# Initialize the Dash app
app = dash.Dash(__name__)

# Define the layout
app.layout = html.Div([
    html.H1(
        'Pink Morsels Sales Visualizer',
        style={'textAlign': 'center', 'color': '#2c3e50', 'marginTop': 20}
    ),
    
    html.Div([
        dcc.Graph(
            id='sales-line-chart',
            figure=fig
        )
    ], style={'padding': 20})
])

# Run the app
if __name__ == '__main__':
    print("Starting Dash app...")
    print("Go to: http://127.0.0.1:8050/")
    app.run(debug=True, host='127.0.0.1', port=8050)