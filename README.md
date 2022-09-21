# Full-text Search with Django and Postgres
Using a django orm and postgres full text search I have implemented a searching and filtering system.
## Getting Started

First clone the repository from GitHub and switch to the new directory:

    $ https://github.com/sh1mu7/django_search.git
    $ cd django_search
## Setup

Create a virtual environment to install dependencies in and activate it:

    $ virtualenv venv
    $ source env/bin/activate


Install project dependencies:

    (env)$ pip install -r requirements.txt

Then simply apply the migrations:

    $ python manage.py migrate

You can now run the development server:

    $ python manage.py runserver
