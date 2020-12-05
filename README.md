# StockMan Project Api
[![CircleCI](https://circleci.com/gh/Maxcutex/stockman_project.svg?style=svg)](https://circleci.com/gh/Maxcutex/stockman_project)
[![Coverage Status](https://coveralls.io/repos/github/Maxcutex/stockman_project/badge.svg?branch=master)](https://coveralls.io/github/Maxcutex/stockman_project?branch=master)


This backend application serves as an API backend to the StockMan Proj application, which allows users to view news and trends in stocks



https://stockman-api.herokuapp.com/



## Usage
Using  Python download and install the latest version of Python 3+.

The application is built with Python

To clone the respository execute the following command.
```
git clone https://github.com/maxcutex/stockman_project.git
```
Navigate into the cloned project directory.

Edit the `env-sample` file with your gmail credentials and save it as `.env`

Change the parameters in there to your own settings e.g SEND GRID KEY

On the prompt execute the following
```
export $(cat .env)
```


Execute the following code to install all the application dependencies.
```
pip install -r requirements.txt
```

Execute the following code to migrate all data tables/object
```
python manage.py  migrate
```


Execute the following at the command line
```
python manage.py runserver
```

Browse the application in the url
```
http://localhost:8000
```

### Features of Stockman App
- View industries
- View News
- View PriceList
- View Analysis
- View Trends over a period




### Testing
Tests can be run using
```
python manage.py test
```
