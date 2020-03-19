![Django CI](https://github.com/KNaiskes/paymentReminder/workflows/Django%20CI/badge.svg)

# paymentReminder
A simple Web application to keep track of future (and past) payments


## Quick Start

Clone repo

```
$ git clone git@github.com:KNaiskes/paymentReminder.git
```
Install requirements
```
$ cd paymentReminder
$ pip install -r requirements.txt
```

Migrate database models
```
$ python manage.py makemigrations
$ python manage.py migrate
```

Create super user (admin)
```
$ python manage.py createsuperuser
```

Start server
```
$ python manage.py runserver
```
