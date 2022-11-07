# RT TECH APIS

## Setup

The first thing to do is to clone the repository:

```sh
$ git clone https://github.com/jamestha3d/rt_tech2.git
$ cd rt_tech2
```

Create a virtual environment to install dependencies in and activate it:

```sh
$ virtualenv env
$ source env/bin/activate
```
Then install the dependencies:

```sh
(env)$ pip install -r requirements.txt
```
Note the `(env)` in front of the prompt. This indicates that this terminal
session operates in a virtual environment set up by `virtualenv`.

Once `pip` has finished downloading the dependencies:
```sh
(env)$ cd rt_project
(env)$ python manage.py migrate
(env)$ python manage.py runserver
```


And navigate to `http://127.0.0.1:8000/`.

## EDIT DATA
To create super user stop the server with ^C and run
```sh
(env) python manage.py createsuperuser
```
follow the prompt, when done run the server again.
go to `http://127.0.0.1:8000/admin/`

## SIGN UP

`localhost:8000/auth/signup`

## IF USING DOCKER 
Right after cloning the repo, run:

```sh
$ docker compose up
```

navigate to your browser of choice and visit:

`localhost:8000/`

also migrate database and create super user.
