from django.db import models

# Create your models here.
class User(models.Model):
    index = models.IntegerField(primary_key=True, unique=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=20)



class Product(models.Model):
    index = models.IntegerField(primary_key=True, unique=True)
    name = models.CharField(max_length=255)
    price = models.FloatField

