from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, get_user_model, AbstractUser
from django.db import models
from django.forms.widgets import PasswordInput, TextInput
from django import forms

from .models import Record


# - Register a user

class CustomUserCreationForm(UserCreationForm):   
    class Meta(UserCreationForm.Meta):
        model = get_user_model()
        fields = ['username', 'role', 'password1', 'password2']


# - User login


class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=TextInput())
    role = forms.CharField(widget=TextInput())
    password = forms.CharField(widget=PasswordInput())

class CreateRecordForm(forms.ModelForm):
    class Meta:
        model = Record
        fields = ['first_name', 'last_name', 'email', 'role', 'Idea ID', 'Idea name', 'Idea description', 'Idea dependencies', 'Date', 'View Idea', 'Idea Comments', 'Idea Votes']

class UpdateRecordForm(forms.ModelForm):
        model = Record
        fields = ['first_name', 'last_name', 'email', 'role', 'Idea ID', 'Idea name', 'Idea description', 'Idea dependencies', 'Date', 'View Idea', 'Idea Comments', 'Idea Votes']





# - Register/Create a user

class CreateUserForm(UserCreationForm):

    class Meta:

        model = User
        fields = ['username', 'role', 'password1', 'password2']


# - Login a user

class LoginForm(AuthenticationForm):

    username = forms.CharField(widget=TextInput())
    role = forms.CharField(widget=TextInput())
    password = forms.CharField(widget=PasswordInput())


# - Create a record

class CreateRecordForm(forms.ModelForm):

    class Meta:

        model = Record
        fields = ['first_name', 'last_name', 'email', 'role', 'Idea ID', 'Idea name', 'Idea description', 'Idea dependencies', 'Date', 'View Idea', 'Idea Comments', 'Idea Votes']


# - Update a record

class UpdateRecordForm(forms.ModelForm):

    class Meta:

        model = Record
        fields = ['first_name', 'last_name', 'email', 'role', 'Idea ID', 'Idea name', 'Idea description', 'Idea dependencies', 'Date', 'View Idea', 'Idea Comments', 'Idea Votes']