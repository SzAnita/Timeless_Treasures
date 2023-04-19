from rest_framework import serializers
from .models import *

class AntiquesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Antiques
        fields = ('id', 'name','type', 'year', 'description', 'creator', 'link', 'valuation', 'fun_facts')


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name', 'email', 'username', 'password')

class FavoritesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Favorites
        fields = ('id', 'user_id', 'email', 'antique_id', 'type', 'year', 'description', 'link', 'valuation', 'fun_facts')
