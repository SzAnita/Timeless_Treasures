from django import forms
from django.core import validators
import re


class Login(forms.Form):
    email = forms.EmailField(required=True, widget=forms.TextInput(attrs={"placeholder": "Email"}), validators=[validators.EmailValidator])
    pwd = forms.CharField(widget=forms.PasswordInput(attrs={"placeholder": "Password"}), required=True, min_length=8)


class Signup(forms.Form):
    email = forms.EmailField(required=True, widget=forms.TextInput(attrs={"placeholder": "Email*"}))
    pwd = forms.CharField(widget=forms.PasswordInput(attrs={"placeholder": "Password*"}), required=True, label='Password', min_length=8)
    fname = forms.CharField(required=False, widget=forms.TextInput(attrs={"placeholder": "First Name"}))
    lname = forms.CharField(required=False, widget=forms.TextInput(attrs={"placeholder": "Last Name"}))
    username = forms.CharField(required=False, widget=forms.TextInput(attrs={"placeholder": "Username"}))
