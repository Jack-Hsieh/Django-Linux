from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

#==============#include login username in ContactForm================
from django.contrib import admin 
from django.contrib.auth import authenticate
from django.contrib import auth
#==============導入時間,用以設定ContactForm的DateTimeField=============
from django.db import models
from django.utils import timezone 
#====================================================================
# Create your form here.

from users.models import Request

# Create your form here.

class RegisterForm(UserCreationForm):
	email = forms.EmailField()
	class Meta:
		model = User
		fields = ["username", "email", "password1", "password2"]


class ContactForm(forms.ModelForm):
    class Meta:
        model = Request
        fields = ('username','email','comment')
