# ======================================================= #
# ======================IMPORTS========================== #
# ======================================================= #
from dash import dash, html, dcc, Input, Output
import dash_bootstrap_components as dbc
from dash_bootstrap_templates import load_figure_template
import pandas as pd
import os
import glob
import altair as alt
alt.data_transformers.enable('data_server')
alt.renderers.set_embed_options(theme='dark')

# ======================================================= #
# ========================SETUP========================== #
# ======================================================= #
# app = dash.Dash(__name__)
app = dash.Dash(external_stylesheets=[dbc.themes.SLATE])
load_figure_template('SLATE')
app.title = 'Driving Diagnostics Dash (TripleD)'

data_path = 'data/processed/'
csv_files = [f for f in os.listdir(data_path) if f.endswith('.csv')]

# ======================================================= #
# ===================HELPER FUNCTIONS==================== #
# ======================================================= #
def concat_df(selected_trips, data_path=data_path):
    dfs = []
    for trip in selected_trips:
        df = pd.read_csv(data_path+trip)
        df['Trip ID'] = trip.replace('.csv', '')
        dfs.append(df)
    return pd.concat(dfs, axis=0)

# ======================================================= #
# ======================APP LAYOUT======================= #
# ======================================================= #
app.layout = dbc.Container([
    html.H1('Driving Diagnostics Dash (TripleD)'),
    dbc.Row([
        html.Label([
            'Select Trips to Examine:',
            dcc.Dropdown(id='trip_dropdown',
                     options=[{'label': f.replace('.csv', ''), 'value': f} for f in csv_files],
                     value=csv_files[0:2],
                     multi=True)
        ])
    ]),
    dbc.Row([
        dbc.Col(
            dbc.Card([
                dbc.CardHeader('Vehicle Speed vs. Time by Trip'),
                dbc.CardBody(
                    html.Iframe(id='speed',
                                style={'border-width': '0', 'width': '100%', 'height': '400px'})
                )
            ])
        ),
        dbc.Col(
            dbc.Card([
                dbc.CardHeader('Lateral Acceleration vs. Time by Trip'),
                dbc.CardBody(
                    html.Iframe(id='lat_acc',
                                style={'border-width': '0', 'width': '100%', 'height': '400px'})
                )
            ])
        )
    ]),
    dbc.Row([
        dbc.Col(
            dbc.Card([
                dbc.CardHeader('Engine Speed vs. Vehicle Speed by Gear'),
                dbc.CardBody(
                    html.Iframe(id='gear',
                                style={'border-width': '0', 'width': '100%', 'height': '400px'})
                )
            ])
        ),
        dbc.Col(
            dbc.Card([
                dbc.CardHeader('Engine Load vs. Engine Speed by Gear'),
                dbc.CardBody(
                    html.Iframe(id='load',
                       style={'border-width': '0', 'width': '100%', 'height': '400px'})
                )
            ])
        )
    ])
])

# ======================================================= #
# ====================APP CALLBACKS====================== #
# ======================================================= #
@app.callback(
    Output('speed', 'srcDoc'),
    Input('trip_dropdown', 'value'))
def plot_speed(selected_trips):
    df = concat_df(selected_trips)
    chart = alt.Chart(df).mark_line().encode(
        x = 'Time (s)',
        y = 'Speed (m/s)',
        color = 'Trip ID',
        tooltip = ['Speed (m/s)', 'Time (s)', 'Trip ID']
    ).interactive()
    return chart.to_html()

@app.callback(
    Output('lat_acc', 'srcDoc'),
    Input('trip_dropdown', 'value'))
def plot_gear(selected_trips):
    df = concat_df(selected_trips)
    chart = alt.Chart(df).mark_line().encode(
        x = 'Time (s)',
        y = 'Lateral Acc (m/s^2)',
        color = 'Trip ID',
        tooltip = ['Lateral Acc (m/s^2)', 'Time (s)', 'Trip ID']
    ).interactive()
    return chart.to_html()

@app.callback(
    Output('gear', 'srcDoc'),
    Input('trip_dropdown', 'value'))
def plot_gear(selected_trips):
    df = concat_df(selected_trips)
    df = df[df.Gear != 0]
    chart = alt.Chart(df).mark_point().encode(
        x = 'Speed (m/s)',
        y = 'Engine RPM',
        color = 'Gear'
    )
    return chart.to_html()

@app.callback(
    Output('load', 'srcDoc'),
    Input('trip_dropdown', 'value'))
def plot_gear(selected_trips):
    df = concat_df(selected_trips)
    df = df[df.Gear != 0]
    chart = alt.Chart(df).mark_point().encode(
        x = 'Gear',
        y = 'Total Acc (m/s^2)',
        color = 'Gear'
    )
    return chart.to_html()

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)