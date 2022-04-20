# from django.db import models

# # Create your models here.

# from django import forms
# from django.contrib.auth.models import User
# from django.contrib.auth.forms import UserCreationForm

# import the standard Django Model
# from built-in library
from django.db import models

class GeeksModel(models.Model):
		
	title = models.CharField(max_length = 200, null=True, blank=True)
	description = models.TextField(null=True, blank=True)
	# last_modified = models.DateTimeField(auto_now_add = True)
	image = models.ImageField(upload_to='images/',null=True,blank=True)
	def __str__(self):
		return self.title

class FormData(models.Model):
    name= models.CharField(max_length =200)
    
    
    def __str__(self):
        return self.name
    
