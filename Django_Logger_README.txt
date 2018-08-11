This will be a web application that allows a user to log entries
about topics they are intersted in and what they have learned so far about each topic.

HOMEPAGE: Describes the site and invites users to either register or log in.

LOGGED IN: User can create new topics, add new entries, and read and edit existing entries. 

1. Developed using a virtual environment: https://packaging.python.org/guides/installing-using-pip-and-virtualenv/
# Create virtual env: py -m virtualenv env
# Activate virtual env: .\env\Scripts\activate
# Deactivate virtual env: deactivate

2. Create a django project using: django-admin startproject <app_name> .
# Creates 3 py files:
# settings.py: controls how django interacts with the system and manages the project
# urls.py: tells Django which pages to build in response to browser requests (Could we used for analytic responses)
# wsgi.py (web server gateway interface): helps Django serve the files it creates

3. Creating the database: 
# Makes sure db matches the current state of the project: python manage.py migrate
# Creates a SQLite DB by default (db.sqlite3) --> Explore using MongoDB
# Any modification to a db is considered a migration


4. Viewing the project
# Use comamnd to check status of app: python manage.py runserver
# can change port using python manage.py runserver 800#
"""
Performing system checks...

System check identified no issues (0 silenced).
August 10, 2018 - 21:09:09
Django version 2.1, using settings 'learn_log.settings'
Starting development server at http://127.0.0.1:8000/ -- Url where project is being served
Quit the server with CTRL-BREAK.
"""


5. Starting the App:
# Open new command line and activate virtual env: .\ll_env\Scripts\activate
# Tell Django to create the infrastructure needed to build an app: python manage.py startapp learn_logs
# creates a new folder with the files:
# models.py: define the data we want to manage in our app
# admin.py
# views.py

# Our model data
# User (unique id)
# topics (varchar2)
# entry (id): 1 to many relationship to topics
# comment (blob): can be updated/deleted
# timestamp of the edit/creation

6. To use models we need to tell Django to include our app in the project
# settings.py: shows apps Django installed in the project
# Update the INSTALLED APPS to include our app

7. Need to run migrate to tell model about our new Topic model class for the app:
# python manage.py makemigrations learn_logs

"""
Migrations for 'learn_logs':
  learn_logs\migrations\0001_initial.py #  migration file created by Django
    - Create model Topic	# creates Topic table in db
"""

8. Apply the migration to the db and have Django perform the update to th db
python manage.py migrate

"""
Operations to perform:
  Apply all migrations: admin, auth, contenttypes, learn_logs, sessions
Running migrations:
  Applying learn_logs.0001_initial... OK
"""

# In summary:
# Steps to modify data in db
# 1. Modify models.py to add / edit models
# 2. call makemigrations on app to create change file
# 3. migrate to have Django apply the updates to db