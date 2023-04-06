from django.shortcuts import render
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