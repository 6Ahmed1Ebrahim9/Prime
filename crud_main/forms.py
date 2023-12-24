from django.contrib.auth.forms import UserCreationForm 
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.forms.widgets import PasswordInput, TextInput

from django import forms
# Register Form/Create User Form

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']
        
# Login Form

class Loginform(AuthenticationForm):
    username = forms.CharField(widget=TextInput(attrs={'class':'validate','placeholder': 'Username'})) # class validate is for materializecss so that the input field is not red
    password = forms.CharField(widget=PasswordInput(attrs={'placeholder':'Password'}))
    class Meta:
        model = User
        fields = ['username', 'password']
