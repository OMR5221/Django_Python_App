from django.db import models

# Topic inherits from Model:
class Topic(models.Model):
	"""A topic the user is learning about: """
	comment = models.CharField(max_length=200)
	date_added = models.DateTimeField(auto_now_add=True) # tells Django to set this attribute to the curr date/time
	date_updated = models.DateTimeField(auto_now=True) # auto_now: changes every time object is saved
	
	def __str__(self):
		"""Return string representation of the model"""
		return self.comment
