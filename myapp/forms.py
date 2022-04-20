from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import GeeksModel, FormData



class UserRegisterForm(UserCreationForm):
	email = forms.EmailField()
	phone_no = forms.CharField(max_length = 20)
	first_name = forms.CharField(max_length = 20)
	last_name = forms.CharField(max_length = 20)
	class Meta:
		model = User
		fields = ['username', 'email', 'phone_no', 'password1', 'password2']
  

class GeeksForm(forms.Form):
	title = forms.CharField(initial = "Method 2")
	description = forms.CharField(initial = "Method 2 Description")
	available = forms.BooleanField(initial = True)
	email = forms.EmailField(initial = "xyz@gmail.com")
 
class DataForm(forms.ModelForm):
    
    class Meta:
        model = GeeksModel
        fields = ['title', 'description', 'image']


class FormDataForm(forms.ModelForm):
    class Meta:
        model = FormData
        fields = '__all__'
  
# def __str__(self):
    # return self.username


# class GeeksForm(forms.ModelForm):
#     # specify the name of model to use
#     class Meta:
#         model = GeeksModel
#         fields = "__all__"