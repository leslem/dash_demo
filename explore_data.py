#!/usr/bin/env/python

import pandas as pd
import plotly.express as px
from palmerpenguins import load_penguins

# Load penguins data set
penguins = load_penguins()
penguins.head()
penguins.info()
penguins.describe()

penguins.groupby(["species"]).size()
penguins[['species', 'year']].groupby(["species"]).count()
penguins[['species']].groupby(["species"]).count()
tmp = penguins[['species']].value_counts()

penguins.groupby(["species"]).describe()
penguins.iloc[:, [0] + list(range(2, 6))]
penguins.iloc[:, [0] + list(range(2, 6))].groupby(["species"]).mean()

