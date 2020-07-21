from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
# from django import forms
from .models import Todo



class CreateUserForm(UserCreationForm):
	class Meta:
		model=User
		fields=['username','email','password1','password2']

class AddTodos(ModelForm):
	class Meta:
		model=Todo
		fields=['content']