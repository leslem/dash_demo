#!/usr/bin/env python

# Add bootstrap styling and some basic UI design

import dash_bootstrap_components as dbc
import pandas as pd
import plotly.express as px
from dash import Dash, html, dash_table, dcc, callback, Output, Input
from palmerpenguins import load_penguins

# Load penguins data set
penguins = load_penguins()
penguin_numeric_cols = penguins.select_dtypes(include=['int16', 'int32', 'int64', 'float16', 'float32', 'float64']).columns

# Initialize the app (with a Bootstrap theme)
# Other themes: CERULEAN, COSMO, CYBORG, DARKLY, FLATLY, JOURNAL, LITERA, LUMEN, LUX, MATERIA, MINTY, MORPH, PULSE, QUARTZ, SANDSTONE, SIMPLEX, SKETCHY, SLATE, SOLAR, SPACELAB, SUPERHERO, UNITED, VAPOR, YETI, ZEPHYR
# Changing theme requires reloading the app
external_stylesheets = [dbc.themes.FLATLY]
app = Dash(__name__, external_stylesheets=external_stylesheets)

# Design app layout (ui)
app.layout = dbc.Container([
	dbc.Row([html.Div(html.H1('Penguins demo app!'), className='text-primary text-center fs-3')]),
	dbc.Row([
		dbc.Col([
			html.H2('Penguins data set'),
			# Try it with theme superhero
			# Bootstrap styles don't seem to apply to the dash_table, so use dbc.Table instead
			dash_table.DataTable(data=penguins.to_dict('records'), page_size=15),
			# But dbc.Table doesn't have paging...
			# dbc.Table.from_dataframe(penguins, striped=True, bordered=True, hover=True),
			], width=9),
		dbc.Col([
			html.H2('Penguin species counts'),
			dcc.Graph(figure=px.histogram(penguins, x='species', y='year', histfunc='count')),
			], width=3),
	]),
	dbc.Row([
		dbc.Col([
			html.H2('Select a column name'),
			dcc.RadioItems(options=penguin_numeric_cols, value=penguin_numeric_cols[0], id='controls-and-radio-item')
			], width=3),
		dbc.Col([
			html.H2('Mean of selected column, by species'),
			dcc.Graph(figure={}, id='controls-and-graph'),
			], width=9),
		]),
], fluid=True)

# Add controls and reactivity
@callback(
	Output(component_id='controls-and-graph', component_property='figure'),
	Input(component_id='controls-and-radio-item', component_property='value')
)
def update_graph(col_chosen):
	fig=px.histogram(penguins, x='species', y=col_chosen, histfunc='avg')
	return fig

# Run the app
if __name__ == '__main__':
	app.run(debug=True)
