import json
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from rest_framework import viewsets
from .serializers import *
from .models import *

class AntiquesView(viewsets.ModelViewSet):

	serializer_class = AntiquesSerializer
	queryset = Antiques.objects.all()