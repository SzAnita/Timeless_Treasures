from django.db import models

# Create your models here.
class User(models.Model):
    index = models.IntegerField(primary_key=True, unique=True, null=False)
    first_name = models.CharField(max_length=255, null=False)
    last_name = models.CharField(max_length=255, null=False)
    email = models.CharField(max_length=255, null=False)
    username = models.CharField(max_length=20, null=False)
    password = models.CharField(max_length=20, null=False)


class Antiques(models.Model):
    index = models.IntegerField(primary_key=True, unique=True, null=False)
    type = models.CharField(max_length=100, null=False)
    year = models.IntegerField(null=False)
    description = models.CharField(max_length=255, null=False)
    valuation = models.FloatField(max_length=12)
    fun_facts = models.CharField(max_length=255, null=True)

