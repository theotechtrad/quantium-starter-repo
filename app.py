import dash
from dash import dcc, html, Input, Output
import pandas as pd
import plotly.express as px

# Read the formatted data
df = pd.read_csv('formatted_data.csv')

# Convert date to datetime and sort
df['date'] = pd.to_datetime(df['date'])
df = df.sort_values('date')

# Initialize the Dash app
app = dash.Dash(__name__)

# Define the layout with styling
app.layout = html.Div([
    # Header
    html.Div([
        html.H1(
            'Pink Morsels Sales Visualizer',
            style={
                'textAlign': 'center',
                'color': '#ffffff',
                'padding': '30px',
                'margin': '0',
                'fontFamily': 'Arial, sans-serif',
                'fontSize': '42px',
                'fontWeight': 'bold'
            }
        )
    ], style={
        'backgroundColor': '#e91e63',
        'marginBottom': '30px',
        'boxShadow': '0 4px 6px rgba(0,0,0,0.1)'
    }),
    
    # Radio button container
    html.Div([
        html.Label(
            'Select Region:',
            style={
                'fontSize': '18px',
                'fontWeight': 'bold',
                'color': '#333',
                'marginRight': '20px',
                'fontFamily': 'Arial, sans-serif'
            }
        ),
        dcc.RadioItems(
            id='region-filter',
            options=[
                {'label': ' All Regions', 'value': 'all'},
                {'label': ' North', 'value': 'north'},
                {'label': ' East', 'value': 'east'},
                {'label': ' South', 'value': 'south'},
                {'label': ' West', 'value': 'west'}
            ],
            value='all',
            inline=True,
            style={
                'fontSize': '16px',
                'fontFamily': 'Arial, sans-serif'
            },
            inputStyle={
                'marginRight': '5px',
                'marginLeft': '15px'
            },
            labelStyle={
                'marginRight': '20px',
                'cursor': 'pointer'
            }
        )
    ], style={
        'textAlign': 'center',
        'padding': '20px',
        'backgroundColor': '#f8f9fa',
        'borderRadius': '10px',
        'margin': '0 auto 30px auto',
        'width': '80%',
        'boxShadow': '0 2px 4px rgba(0,0,0,0.1)'
    }),
    
    # Chart container
    html.Div([
        dcc.Graph(
            id='sales-line-chart',
            style={'height': '500px'}
        )
    ], style={
        'padding': '20px',
        'backgroundColor': '#ffffff',
        'borderRadius': '10px',
        'margin': '0 auto',
        'width': '90%',
        'boxShadow': '0 2px 8px rgba(0,0,0,0.1)'
    })
], style={
    'backgroundColor': '#f0f2f5',
    'minHeight': '100vh',
    'padding': '0',
    'margin': '0',
    'fontFamily': 'Arial, sans-serif'
})

# Callback to update the chart based on region selection
@app.callback(
    Output('sales-line-chart', 'figure'),
    Input('region-filter', 'value')
)
def update_chart(selected_region):
    # Filter data based on selected region
    if selected_region == 'all':
        filtered_df = df
        title = 'Pink Morsels Daily Sales - All Regions'
    else:
        filtered_df = df[df['region'] == selected_region]
        title = f'Pink Morsels Daily Sales - {selected_region.capitalize()} Region'
    
    # Group by date to get total sales per day
    daily_sales = filtered_df.groupby('date')['sales'].sum().reset_index()
    
    # Create the line chart
    fig = px.line(
        daily_sales,
        x='date',
        y='sales',
        title=title,
        labels={
            'date': 'Date',
            'sales': 'Sales ($)'
        },
        markers=True
    )
    
    # Customize the chart appearance
    fig.update_traces(
        line_color='#e91e63',
        line_width=3,
        marker=dict(size=8, color='#c2185b')
    )
    
    fig.update_layout(
        xaxis_title='Date',
        yaxis_title='Sales ($)',
        hovermode='x unified',
        plot_bgcolor='#fafafa',
        paper_bgcolor='#ffffff',
        font=dict(family='Arial, sans-serif', size=12, color='#333'),
        title_font=dict(size=20, color='#333', family='Arial, sans-serif'),
        xaxis=dict(
            showgrid=True,
            gridcolor='#e0e0e0',
            showline=True,
            linecolor='#333'
        ),
        yaxis=dict(
            showgrid=True,
            gridcolor='#e0e0e0',
            showline=True,
            linecolor='#333'
        )
    )
    
    return fig

# For deployment
server = app.server

if __name__ == '__main__':
    print("Starting Dash app...")
    print("Go to: http://127.0.0.1:8050/")
    app.run(debug=True, host='127.0.0.1', port=8050)