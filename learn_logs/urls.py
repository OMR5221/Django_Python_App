"""Defines URL patterns for learning_logs app"""

from django.urls import path

from . import views

app_name = 'learn_logs'
urlpatterns = [
	# Home Page for learn_logs site:
	path('', views.index, name='index'),
]