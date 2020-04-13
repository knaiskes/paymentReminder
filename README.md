![Django CI](https://github.com/KNaiskes/paymentReminder/workflows/Django%20CI/badge.svg)

# paymentReminder
A web application to keep track of future and past payments

## Dependencies

- [Python 3](https://www.python.org/)

## Quick Start

Clone repo

```
$ git clone git@github.com:KNaiskes/paymentReminder.git
```
Create and activate virtual enviroment
```
$ python -m venv venv
$ source venv/bin/activate
```
Install requirements
```
$ cd paymentReminder
$ pip install -r requirements.txt
```

Migrate database models
```
$ python manage.py makemigrations payments
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
Visit
```
localhost:8000/
```

## License
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
