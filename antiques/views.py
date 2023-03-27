import json
from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from .models import User, Antiques


# Create your views here.

def index(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render())


def login(request):
    template = loader.get_template('login.html')
    return HttpResponse(template.render())
def check_user(request):
    email = request.POST.get('email')
    pwd = request.POST.get('pwd')
    user = User.objects.get(password=pwd, email=email)
    msg =''
    if user is None:
        msg = 'invalid'
    else:
        if user.admin:
            msg = 'admin'
        else:
            msg = 'customer'
    return HttpResponse(json.dumps(msg))
