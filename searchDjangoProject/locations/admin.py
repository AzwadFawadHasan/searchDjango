from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Country, State, Place

admin.site.register(Country)
admin.site.register(State)
admin.site.register(Place)
