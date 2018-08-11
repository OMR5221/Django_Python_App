This will be a web application that allows a user to log entries
about topics they are intersted in and what they have learned so far about each topic.

HOMEPAGE: Describes the site and invites users to either register or log in.

LOGGED IN: User can create new topics, add new entries, and read and edit existing entries. 

# 1. Developed using a virtual environment: https://packaging.python.org/guides/installing-using-pip-and-virtualenv/
# Create virtual env: py -m virtualenv env
# Activate virtual env: .\env\Scripts\activate
# Deactivate virtual env: deactivate

# 2. Create a django project using: django-admin startproject <app_name> .
# Creates 3 py files:
# settings.py: controls how django interacts with the system and manages the project
# urls.py: tells Django which pages to build in response to browser requests (Could we used for analytic responses)
# wsgi.py (web server gateway interface): helps Django serve the files it creates

# 3. Creating the database: 
# Makes sure db matches the current state of the project: python manage.py migrate
# Creates a SQLite DB by default (db.sqlite3) --> Explore using MongoDB
# Any modification to a db is considered a migration


# 4. Viewing the project
# Use comamnd to check status of app: python manage.py runserver
# can change port using python manage.py runserver 800#
/*
Performing system checks...

System check identified no issues (0 silenced).
August 10, 2018 - 21:09:09
Django version 2.1, using settings 'learn_log.settings'
Starting development server at http://127.0.0.1:8000/ -- Url where project is being served
Quit the server with CTRL-BREAK.
*/