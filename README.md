# README

### This is a simple app, MoviesGalore, which represents my introduction and first attempt using Django . 


* Python version: 3.6.0

* Django version: 1.10.6

* System dependencies: This app requires sqlite3 as a database. All other dependencies are listed in setting.py under INSTALLED_APPS.

* Database Configuration: once you have cloned the repo and updated for gems, you will have to set up the database on your local machine. * To do this, please run the following commands from your terminal in order:
<br>
`python manage.py migrate` (this will create the database needed to run the project from the migrations)  
`python manage.py seed movies --number__` (this will load fake seed data into the database for each model, with the `number=__` specifying the amount of fake data you want for the models)  

* How to run the program from your local browser: if you would like to run the program from your browser, please type `python manage.py runserver` into the terminal and then open up a browser of your choice and type in the following basic URL `localhost:8000/movies` or `http://127.0.0.1:8000/movies`. The following extra paths are also available: 

####Database Endpoints
`localhost:8000/movies` returns a list of all movies in the database  
`localhost:8000/movies/actors`  returns a list of all actors in the database  
`localhost:8000/movies/load` loads a new movie into the database  
`localhost:8000/movies/loadactor` loads a new actor into the database  
`localhost:8000/movies/loadjoin` loads a new movie/actor relationship into the database  
`localhost:8000/movies/actortable` takes an actor from a dropdown menu and, upon clicking submit, returns a table with all of the specified actor's movies from the database  



