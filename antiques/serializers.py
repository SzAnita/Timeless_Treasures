from rest_framework import serializers
from .models import *


class AntiquesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Antiques
        fields = ('id', 'name', 'type', 'year', 'description', 'creator', 'link', 'valuation')


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name', 'email', 'username', 'pwd')


class FavoritesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Favorites
        fields = ('id', 'user_id', 'antique_id')


class CollectionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Collections
        fields = ('id', 'user_id', 'name')


class AntiquesCollectionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = AntiquesCollections
        fields = ('id', 'user_id', 'antique_id', 'collection_id')
