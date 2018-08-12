"""Defines URL patterns for learning_logs app"""

# import path function to map url to views:
from django.urls import path

# import all of the views for the app
from . import views

# Helps Django differentiate this urls.py file from others:
app_name = 'learn_logs'

# pages that can be requested from the app:
urlpatterns = [
	# Home Page for learn_logs site:
	# param 1: string to help Django route the current request properly when matched calls the 2nd aparam
	# param 2: specify the view function to call
	# param 3: a name we can reference this url by in the rest of the code
	path('', views.index, name='index'),
]
