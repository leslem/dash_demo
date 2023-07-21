#!/usr/bin/env python

# A simple app with a reactive graph, where you can choose the data column to
# be shown in the graph

import pandas as pd
import plotly.express as px
from dash import Dash, html, dash_table, dcc, callback, Output, Input
from palmerpenguins import load_penguins

# Load penguins data set
penguins = load_penguins()
penguin_numeric_cols = penguins.select_dtypes(include=['int16', 'int32', 'int64', 'float16', 'float32', 'float64']).columns

# Initialize the app
app = Dash(__name__)

# Design app layout (ui)
app.layout = html.Div([
	html.Div(children='Penguins demo app'),
	html.H2('Penguins data set'),
	dash_table.DataTable(data=penguins.to_dict('records'), page_size=15),
	html.H2('Penguin species counts'),
	dcc.Graph(figure=px.histogram(penguins, x='species', y='year', histfunc='count')),
	html.H2('Pick your mean'),
	dcc.RadioItems(options=penguin_numeric_cols, value=penguin_numeric_cols[0], id='controls-and-radio-item'),
	dcc.Graph(figure={}, id='controls-and-graph'),
])

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
