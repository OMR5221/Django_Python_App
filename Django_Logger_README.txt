This will be a web application that allows a user to log entries
about topics they are intersted in and what they have learned so far about each topic.

HOMEPAGE: Describes the site and invites users to either register or log in.

LOGGED IN: User can create new topics, add new entries, and read and edit existing entries. 

1. Developed using a virtual environment: https://packaging.python.org/guides/installing-using-pip-and-virtualenv/
# Create virtual env: py -m virtualenv ll_env
# Activate virtual env: .\ll_env\Scripts\activate
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
# Use command to check status of app: python manage.py runserver
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

9. Create User accounts
# SuperUser (Admin): python manage.py createsuperuser
# username: ll_admin
# pswd: 

# Default models in Django for admin: User and Group
# admin.py: register models here for the admin user 

"""
# Imports the model we wnat to register 

from learn_logs.models import Topic

# Tells Django to manage our model through the admin site:

admin.site.register(Topic)
"""

10. Added Entry model
# Migrate to incorporate changes: python manage.py makemigrations leanr_logs
# Commit updates to db: python manage.py migrate

11. Need to register the Entry model with the admin
# admin.site.register(Entry)
# Add entries via the admin GUI in the frontend

12. Open a python shell to explore data
# python manage.py shell -- Open a python shell
# from learn_logs.models import Topic -- load Topic table
# Topic.objects.all() -- Get all instances of Topic objects

"""
Output:

<QuerySet [<Topic: Python>, <Topic: Django>, <Topic: Java>]>
"""

# We can loop over this list of Topic objects:
topics = Topic.objects.all()
for topic in topics:
	print(topic.id, topic)

# Can also get a individual topic item by index:
t = Topic.objects.get(id=1)
t.name
t.date_added

# We can get the entries associted to this topic via a foreign key:
t.entry_set.all()

# Windows CTRL-Z & ENTER to exit shell

13. Remap URLs
# Change homepage url in urls.py