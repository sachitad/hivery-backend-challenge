# Paranuara Project Installation Guide

### Installation
This program uses Python3.
If you don't already have virtualenv install it, if you have mkvirtualenv even better.
`sudo pip install virtualenv`

Create virtualenv with python3:
`virtualenv paranuara --python=/usr/local/bin/python3`

Activate the virtualenv - skip if you are using mkvirtualenv:
`source paranuara/bin/activate`

Install the dependencies:
`pip install -r requirements.txt`

Create database and table (uses default sqlite3):
`python manage.py migrate`

We have two resources file: people.json and company.json which contains the initial data. Let's load that up into our newly created database.
`python manage.py load_db_from_json`

We are done! Let's run the server
`python manage.py localhost:8000`