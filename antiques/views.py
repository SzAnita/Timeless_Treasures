import json
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from rest_framework import viewsets
from rest_framework.response import Response
from .serializers import *
from .models import *
from .forms import *

class AntiquesView(viewsets.ModelViewSet):

    queryset = Antiques.objects.all()
    serializer_class = AntiquesSerializer

class UserView(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()

class FavoritesView(viewsets.ModelViewSet):
    serializer_class = FavoritesSerializer
    queryset = Favorites.objects.all()

def index(request):
    context = {
        'antiques': Antiques.objects.all().values()
    }
    template = loader.get_template('index.html')
    return HttpResponse(template.render(context, request))


def login(request):
    template = loader.get_template('login.html')
    context = {
        'form': Login
    }
    if request.method == 'POST':
        email = request.POST.get('email')
        pwd = request.POST.get('pwd')
        try:
            user = User.objects.filter(email=email, pwd=pwd).get()
            if 'email' not in request.session:
                request.session['email'] = email
            template = loader.get_template('index.html')
            context = {
                'antiques': Antiques.objects.all().values(),
            }
            return HttpResponseRedirect(template.render(context, request))
        except User.DoesNotExist:
            template = loader.get_template('login.html')
            context = {
                'form': Login,
                'valid': 'no'
            }
    return HttpResponse(template.render(context, request))

def signup(request):
    template = loader.get_template('signup.html')
    return HttpResponse(template.render({'form':Signup}, request))

def add_user(request):
    email = request.POST.get('email')
    pwd = request.POST.get('pwd')
    fname = request.POST.get('fname')
    lname = request.POST.get('lname')
    user = User(email=email, pwd=pwd, first_name=fname, last_name=lname)
    user.save()

    request.session['email'] = email
    return HttpResponseRedirect('index')

