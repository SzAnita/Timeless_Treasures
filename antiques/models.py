from django.db import models

# Create your models here.
class User(models.Model):
    id = models.IntegerField(primary_key=True, unique=True)
    first_name = models.CharField(max_length=255, null=True)
    last_name = models.CharField(max_length=255, null=True)
    email = models.EmailField(max_length=255, null=False, unique=True)
    username = models.CharField(max_length=20, null=True, unique=True)
    pwd = models.CharField(max_length=20, null=False)


class Antiques(models.Model):
    id = models.IntegerField(primary_key=True, unique=True)
    name = models.CharField(max_length=255)
    type = models.CharField(max_length=50)
    year = models.CharField(max_length=100)
    description = models.CharField(max_length=255)
    creator = models.CharField(max_length=150)
    link = models.CharField(max_length=255)
    valuation = models.CharField(max_length=255, null=True)
    fun_facts = models.CharField(max_length=255, null=True)

class Favorites(models.Model):
    id = models.IntegerField(primary_key=True, unique=True)
    user_id = models.ForeignKey('User', on_delete=models.SET_NULL, null=True)
    antique_id = models.ForeignKey('Antiques', on_delete=models.SET_NULL, null=True)


