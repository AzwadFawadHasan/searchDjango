from django.db import models

# Create your models here.
from django.db import models

class Country(models.Model):
    name = models.CharField(max_length=255)

class State(models.Model):
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)

class Place(models.Model):
    state = models.ForeignKey(State, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)

