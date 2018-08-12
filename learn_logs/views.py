# Renders the response based on the data provided by views:
from django.shortcuts import render

# when url matches the pattern defined Django will look for a fucntion called index() here:
def index(request):

  """The home page for Learn Logs"""
  # Param 1: the original request by user
  # Param 2: the template to be called
  return render(request, 'learn_logs/index.html')
