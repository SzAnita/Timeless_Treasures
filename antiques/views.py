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
import re


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
            if 'email' not in request.session or request.session['email'] == "logout":
                request.session['email'] = email
                request.session.modified = True
            template = loader.get_template('index.html')
            context = {
                'antiques': Antiques.objects.all().values(),
                'email': email
            }
            return HttpResponseRedirect('index')
        except User.DoesNotExist:
            template = loader.get_template('login.html')
            context = {
                'form': Login,
                'valid': 'no'
            }
    return HttpResponse(template.render(context, request))


def signup(request):
    context = {
        'form': Signup
    }
    if request.method == 'POST':
        email = request.POST.get('email')
        pwd = request.POST.get('pwd')
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        valid = True
        data = {
            'email': email,
            'pwd': pwd,
            'fname': fname,
            'lname': lname
        }
        if User.objects.filter(email=email).exists():
            context['valid'] = 'no'
            context['email'] = 'yes'
            context['form'] = Signup(data)
            valid = False
        if not (re.search("[0-9]", pwd) and re.search("[A-Z]", pwd) and (re.search("[*!@#&%_.,$?+=-]", pwd) or re.search("-", pwd))):
            context['valid'] = 'no'
            context['pwd'] = 'yes'
            context['form'] = Signup(data)
        if valid:
            user = User(email=email, pwd=pwd, first_name=fname, last_name=lname)
            user.save()
            request.session['email'] = email
            request.session.modified = True
            return HttpResponseRedirect('index')
    template = loader.get_template('signup.html')
    return HttpResponse(template.render(context, request))


def search(request, kind):
    context = {
        'antiques':Antiques.objects.filter(type=kind)
    }
    template = loader.get_template('index.html')
    return HttpResponse(template.render(context, request))


def add_favorite(request, name):
    if 'email' in request.session and request.session['email'] != "logout":
        email = request.session.get('email')
        user_id = User.objects.get(email=email)
        antique_id = Antiques.objects.get(name=name)
        fav = Favorites(user_id=user_id, antique_id=antique_id)
        fav.save()
        return HttpResponseRedirect('index')
    else:
        return HttpResponseRedirect('../login')


def logout(request):
    request.session['email'] = "logout"
    request.session.modified = True
    return HttpResponseRedirect('index')




