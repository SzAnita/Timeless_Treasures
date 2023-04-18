from django.db import models

# Create your models here.
class User(models.Model):
    id = models.IntegerField(primary_key=True, unique=True, null=False)
    first_name = models.CharField(max_length=255, null=False)
    last_name = models.CharField(max_length=255, null=False)
    email = models.CharField(max_length=255, null=False)
    username = models.CharField(max_length=20, null=False)
    password = models.CharField(max_length=20, null=False)


class Antiques(models.Model):
    id = models.IntegerField(primary_key=True, unique=True)
    type = models.CharField(max_length=100)
    year = models.CharField(max_length=50, null=True)
    description = models.CharField(max_length=255)
    link = models.CharField(max_length=255, null=True)
    valuation = models.FloatField(max_length=12)
    fun_facts = models.CharField(max_length=255, null=True)

class Favorites(models.Model):
    id = models.IntegerField(primary_key=True, unique=True)
    user_id = models.ForeignKey('User', on_delete=models.SET_NULL, null=True)
    antique_id = models.ForeignKey('Antiques', on_delete=models.SET_NULL, null=True)


