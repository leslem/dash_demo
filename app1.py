#!/usr/bin/env python

# A very simple Hello World Dash app

from dash import Dash, html

# Initialize the app
app = Dash(__name__)

# Design app layout (ui)
app.layout = html.Div([
	html.Div(children='Hello World!')
])

# Run the app
if __name__ == '__main__':
	app.run(debug=True)
