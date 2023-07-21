#!/usr/bin/env python

# A simple dash app with the penguins data, a table, and a graph

import pandas as pd
import plotly.express as px
from dash import Dash, html, dash_table, dcc
from palmerpenguins import load_penguins

# Load penguins data set
penguins = load_penguins()


# Initialize the app
app = Dash(__name__)

# Design app layout (ui)
app.layout = html.Div([
	html.Div(children='Penguins demo app'),
	html.H2('Penguins data set'),
	dash_table.DataTable(data=penguins.to_dict('records'), page_size=15),
	html.H2('Penguin species counts'),
	dcc.Graph(figure=px.histogram(penguins, x='species', y='year', histfunc='count')),
	html.H2('Mean bill length by species'),
	# Try 'median' or 'mean' for an interesting error message
	dcc.Graph(figure=px.histogram(penguins, x='species', y='bill_length_mm', histfunc='avg'))
])

# Run the app
if __name__ == '__main__':
	app.run(debug=True)
