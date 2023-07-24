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
- Hello World app (`app1.py`)
	- Notice that it doesn't have any default styling
- Add a table and a graph of penguins data (`app2.py`)
- Add reactivity (`app3.py`)
- Add Bootstrap styling (`app4.py`)
- Deploy to Posit Connect

## Dash vs. Shiny
- Dash `app.layout` object is like Shiny `ui()` function
- Dash is built around `plotly` visualizations (made by same company)
	- Shiny is more general, and not tied to specific R packages
- Dash is a little more "low level" (despite being built on top of another Python web framework, `flask`)
- For R, Shiny is pretty much the only game in town, while Dash is just one of many Python web frameworks


## Deploy a Dash app to Posit Connect

- **Make sure you used a version of Python that's available on the Connect server!**
	- Find this at the bottom of the "Documentation" page of your server
- Install `rsconnect-python` package via pip
- At the command line, run the deployment command

```
rsconnect deploy dash \
	--title "July 2023 Dash demo app" \
	--server https://myserver.example.com \
	--api-key $CONNECT_API_KEY \
	--entrypoint app4:app \
	.
```

- Note the best documentation is from `rsconnect deploy dash --help`, not from anything on the Posit web content


## Deploy a Dash app to Domino

- TODO
- [Domino Dash deployment docs](https://docs.dominodatalab.com/en/5.3/user_guide/de2589/publish-a-dash-app/)


## Resources
- [Appsilon Dash vs. R Shiny article](https://www.google.com/search?client=safari&rls=en&q=appsilon+dash+vs+shiny&ie=UTF-8&oe=UTF-8)
- [Dash bootstrap components](https://dash-bootstrap-components.opensource.faculty.ai)
- [Posit Connect user guide on deploying Dash apps](https://docs.posit.co/connect/user/dash/)
- [rsconnect-python package documentation]()

