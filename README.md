# dash_demo

This is a demo of the Dash app framework. The content is largely based on this very basic [quickstart tutorial from Dash](https://dash.plotly.com/tutorial).

## Step by step
*This assumes you already have a working Python 3 installation and know about virtual environment*
1. Set up and activate a virtual environment of your choice
	- Install dash and any other packages you plan to use
	- I used `virtualenv` + `virtualenvwrapper`
	- See `make_virtualenv.sh` for my process
1. Write an `app.py` script
1. Run your app from the command line: `python app1.py`
1. Open 

## Demo outline
- Hello World app
	- Notice that it doesn't have any default styling

## Dash vs. Shiny
- Dash `app.layout` object is like Shiny `ui()` function
- Dash is built around `plotly` visualizations (made by same company)
	- Shiny is more general, and not tied to specific R packages
- Dash is a little more "low level" (despite being built on top of another Python web framework, `flask`)
- For R, Shiny is pretty much the only game in town, while Dash is just one of many Python web frameworks



## Deploy a Dash app to Domino


## Deploy a Dash app to Posit Connect


## Resources
- [Appsilon Dash vs. R Shiny article](https://www.google.com/search?client=safari&rls=en&q=appsilon+dash+vs+shiny&ie=UTF-8&oe=UTF-8)
- [Dash bootstrap components](https://dash-bootstrap-components.opensource.faculty.ai)


