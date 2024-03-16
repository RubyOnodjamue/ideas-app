from django.contrib.auth import UserCreationForm, AuthenticationForm
from django.forms.widgets import PasswordInput, TextInput
from django import forms

from .models import Record, User


class BaseRecordForm(forms.ModelForm):
    class Meta:
        model = Record
        fields = ['first_name', 'last_name', 'work_email', 'work_phone', 'address', 'city', 'province', 'country']

# - Register a user

class CreateUserForm(UserCreationForm):   
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']

# - User login


class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=TextInput())
    password = forms.CharField(widget=PasswordInput())

class CreateRecordForm(BaseRecordForm):
    pass

class UpdateRecordForm(BaseRecordForm):
    pass