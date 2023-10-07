from django.db import models

# Create your models here.
from django.db import models

class Country(models.Model):
    name = models.CharField(max_length=200)

class State(models.Model):
    name = models.CharField(max_length=200)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)

class Place(models.Model):
    name = models.CharField(max_length=200)
    state = models.ForeignKey(State, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
