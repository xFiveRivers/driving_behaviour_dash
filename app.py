from dash import dash, html, dcc
import pandas as pd
import os
import glob

# Set up the app and define the title
app = dash.Dash(__name__)
app.title = 'Driving Diagnostics Dash (TripleD)'

# Define the data path
data_path = 'data/processed/'

# Get list of csv files from data path
csv_files = [f for f in os.listdir(data_path) if f.endswith('.csv')]

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)