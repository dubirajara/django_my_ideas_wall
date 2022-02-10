# Share Ideas - My Ideas Wall.
Web app developed using [Django](https://www.djangoproject.com).

Demo: https://shareideas.herokuapp.com

[![Updates](https://pyup.io/repos/github/dubirajara/django_my_ideas_wall/shield.svg)](https://pyup.io/repos/github/dubirajara/django_my_ideas_wall/)
[![Coverage Status](https://coveralls.io/repos/github/dubirajara/django_my_ideas_wall/badge.svg?branch=master)](https://coveralls.io/github/dubirajara/django_my_ideas_wall?branch=master)
[![Python 3](https://pyup.io/repos/github/dubirajara/django_my_ideas_wall/python-3-shield.svg)](https://pyup.io/repos/github/dubirajara/django_my_ideas_wall/)



##

## How Dev? Running locally(virtualenv):

- Clone the repository:

```sh
git clone https://github.com/dubirajara/django_my_ideas_wall.git myideasapp && cd myideasapp
```

- Create and activate virtualenv with Python 3.6+:

```sh
virtualenv .venv
source .venv/bin/activate 
```

- Install the dependencies:
```sh
pip install -r requirements-dev.txt
```
- Set up your local configuration file .env:
```sh
python contrib/config_env.py
```
- Run the migrations and run tests:
```sh
python manage.py migrate
python manage.py test
```

##

## Using Docker to development:

#### Django + Postgresql + Gunicorn + Nginx  

- Clone the repository:

```sh
git clone https://github.com/dubirajara/django_my_ideas_wall.git myideasapp && cd myideasapp
```  
- Set up your Postgresql configuration file:

> Before run the docker container, you must uncomment the line 15 "*DATABASE_URL=*" in file **contrib/secret_gen.py**  
>And if you want config it , change the data to your database config, and too in file **contrib/docker-entrypoint-initdb.d/init_db.sh**

- Build and start services:

```sh
docker-compose up -d --build

```  
  

You can access it at: [`localhost:8000`](localhost:8000)
