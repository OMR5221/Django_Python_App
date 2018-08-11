from django.db import models

# Topic inherits from Model:
class Topic(models.Model):
	"""A topic the user is learning about: """
	name = models.CharField(max_length=200)
	date_added = models.DateTimeField(auto_now_add=True) # tells Django to set this attribute to the curr date/time
		
	def __str__(self):
		"""Return string representation of the model"""
		return self.name

		
# Class for model for entries under a Topic:
class Entry(models.Model):
	"""Specify comment about the topic:"""
	# Associate the entry to the topic model: 
	# on_delete=models.CASCADE: Set to delete all entries when topic is deleted
	topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
	text = models.TextField() # User comment field (no length defined)
	date_added = models.DateTimeField(auto_now_add=True) # Date entry was created
	date_updated = models.DateTimeField(auto_now=True) # auto_now: changes every time object is saved

	# Holds extra info for managing a model
	# We are using to set a special attribute to tell Django to use Entries when it 
	# needs to refer to more than 1 entry:
	# Otherwise Django would refer to multiple entries as "Entrys"
	# Essentially just a Way to change the name of a collection
	class Meta:
		verbose_name_plural = 'entries'
		
	def __str__(self):
		"""Return str representation of the Entry text's 50 first chars:"""
		return self.text[:50] + "..."