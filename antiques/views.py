import json
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from rest_framework import viewsets
from .serializers import *
from .models import *

class AntiquesView(viewsets.ModelViewSet):

	serializer_class = AntiquesSerializer
	queryset = Antiques.objects.all()

class UserView(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()

class FavoritesView(viewsets.ModelViewSet):
    serializer_class = FavoritesSerializer
    queryset = Favorites.objects.all()

def index(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render(), request)

def login(request):
    template = loader.get_template('login.html')
    return HttpResponse(template.render())

