
mkvirtualenv -a ~/devel/dash_demo dash_demo
workon dash_demo

pip install --upgrade pip
pip install dash
pip install pandas
pip install flake8
pip install flake8-docstrings
pip install palmerpenguins
pip install dash-bootstrap-components
pip install rsconnect-python

pip freeze > requirements.txt
