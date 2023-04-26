from django import forms
from django.core import validators
import re

def validate_pwd(pwd):
    if not (re.search("[0-9]", pwd) and re.search("[A-Z]", pwd) and (re.search("[*!@#%_.,$]", pwd) or re.search("-", pwd))):
        raise forms.ValidationError("Not a valid password")


class Login(forms.Form):
    email = forms.EmailField(required=True, label='Email', validators=[validators.EmailValidator])
    pwd = forms.CharField(widget=forms.PasswordInput, required=True, label='Password', min_length=8)

class Signup(forms.Form):
    email = forms.EmailField(required=True, label='Email')
    pwd = forms.CharField(widget=forms.PasswordInput, required=True, label='Password', min_length=8, validators=[validate_pwd])
    pwd2 = forms.CharField(widget=forms.PasswordInput, required=True, label='Confirm password', min_length=8)
    fname = forms.CharField(required=False, label='First Name(optional)')
    lname = forms.CharField(required=False, label='Last Name(optional)')