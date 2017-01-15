## My Ideas Wall web app. Developed using [Django Framework](https://www.djangoproject.com).

Demo: http://shareideas.herokuapp.com

[![Build Status](https://travis-ci.org/dubirajara/django_my_ideas_wall.svg?branch=master)](https://travis-ci.org/dubirajara/django_my_ideas_wall)
[![Code Health](https://landscape.io/github/dubirajara/django_my_ideas_wall/master/landscape.svg?style=flat)](https://landscape.io/github/dubirajara/django_my_ideas_wall/master)
[![Coverage Status](https://coveralls.io/repos/github/dubirajara/django_my_ideas_wall/badge.svg?branch=master)](https://coveralls.io/github/dubirajara/django_my_ideas_wall?branch=master)[![Updates](https://pyup.io/repos/github/dubirajara/django_my_ideas_wall/shield.svg)](https://pyup.io/repos/github/dubirajara/django_my_ideas_wall/)


##

- Clone the repository:

```sh
git clone https://github.com/dubirajara/django_my_ideas_wall.git myideasapp
cd myideasapp
```

- Create and activate virtualenv with Python 3.5:

```sh
virtualenv .venv
source .venv/bin/activate 
```

- Install the dependencies:
```sh
pip install -r requirements.txt
```
- Set up your local configuration file .env:
```sh
cp contrib/env-sample myideas/.env
```
- Run the migrations and run tests:
```sh
python manage.py migrate
python manage.py test
```