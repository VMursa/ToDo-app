from django import forms
from django.contrib.auth.forms import AuthenticationForm

from django import forms
from django.contrib.auth.models import User

class CustomLoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'my-custom-class'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'my-custom-class'}))

