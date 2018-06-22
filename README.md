# Raspi flask server to let the chickens out

## Set up/update
`sudo apt-get update`

`sudo apt-get install python3`

`sudo apt-get install python3-pip`

`sudo apt-get install git`

`sudo pip3 install flask`

`sudo pip3 install Flask-BasicAuth`

## Get the repo
`git clone https://github.com/WoodburyShortridge/raspi_flask.git`

## move to dir
`cd raspi_flask`

## set up auth

`cp example.env.py env.py`

Edit config dict in env.py

## Start the server
`sudo python3 main.py`

## View
visit http://localhost:3000
