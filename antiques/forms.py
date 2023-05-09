from django import forms
from django.core import validators
import re

class Login(forms.Form):
    email = forms.EmailField(required=True, label='Email', validators=[validators.EmailValidator])
    pwd = forms.CharField(widget=forms.PasswordInput, required=True, label='Password', min_length=8)

class Signup(forms.Form):
    email = forms.EmailField(required=True, label='Email')
    pwd = forms.CharField(widget=forms.PasswordInput, required=True, label='Password', min_length=8)
    fname = forms.CharField(required=False, label='First Name(optional)')
    lname = forms.CharField(required=False, label='Last Name(optional)')