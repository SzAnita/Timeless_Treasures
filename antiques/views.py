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
        'antiques': Antiques.objects.all().values(),
        'heart': 'yes'
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
            context['v'] = 'no'
            context['email'] = 'yes'
            context['form'] = Signup(data)
            valid = False
        if not (re.search("[0-9]", pwd) and re.search("[A-Z]", pwd) and (re.search("[*!@#&%_.,$?+=-]", pwd) or re.search("-", pwd))):
            context['v'] = 'no'
            context['p'] = 'yes'
            context['form'] = Signup(data)
        if valid:
            user = User(email=email, pwd=pwd, first_name=fname, last_name=lname)
            user.save()
            request.session['email'] = email
            request.session.modified = True
            return HttpResponseRedirect('index')
    template = loader.get_template('signup.html')
    return HttpResponse(template.render(context, request))


def menu(request, kind):
    context = {
        'antiques': Antiques.objects.filter(type=kind)
    }
    template = loader.get_template('index.html')
    return HttpResponse(template.render(context, request))


def add_favorite(request, name):
    if 'email' in request.session and request.session['email'] != "logout":
        email = request.session.get('email')
        user_ = User.objects.get(email=email)
        antique = Antiques.objects.get(name=name)
        fav = Favorites(user_id=user_, antique_id=antique)
        fav.save()
        return HttpResponseRedirect('../index')
    else:
        return HttpResponseRedirect('../login')


def logout(request):
    request.session['email'] = "logout"
    request.session.modified = True
    return HttpResponseRedirect('index')


def check_user(request):
    if 'email' in request.session and request.session['email'] != "logout":
        return HttpResponseRedirect('user')
    else:
        return HttpResponseRedirect('login')


def user(request):
    if 'email' in request.session and request.session['email'] != "logout":
        user_id = User.objects.get(email=request.session['email'])
        favorite = set()
        for f in Favorites.objects.filter(user_id=user_id).select_related("antique_id"):
            favorite.add(f.antique_id)
        context = {
            'antiques': favorite,
            'heart': 'no',
            'email': request.session['email']
        }
        template = loader.get_template('user.html')
        return HttpResponse(template.render(context, request))
    else:
        #return HttpResponseRedirect('login')
        template = loader.get_template('user.html')
        return HttpResponse(template.render())








