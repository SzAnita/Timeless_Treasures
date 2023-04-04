from rest_framework import serializers
from .models import Antiques, User

class AntiquesSerializer(serializers.ModelSerializer):
    class Meta:
        model1 = Antiques
        fields = ('id', 'type', 'year', 'description', 'valuation', 'fun_facts')