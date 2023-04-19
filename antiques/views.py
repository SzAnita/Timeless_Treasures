import json
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from rest_framework import viewsets
from rest_framework.response import Response
from .serializers import *
from .models import *

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

def get_antiques(request):

    return Antiques.objects.all().values()

def login(request):
    template = loader.get_template('login.html')
    return HttpResponse(template.render())

