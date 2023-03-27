from django.db import models

# Create your models here.
class User(models.Model):
    index = models.IntegerField(primary_key=True, unique=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=20)


class Antiques(models.Model):
    index = models.IntegerField(primary_key=True, unique=True)
    type = models.CharField(max_length=255)
    year = models.IntegerField
    description = models.CharField(max_length=255)
    valuation = models.FloatField(max_length=12)


