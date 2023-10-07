from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView
from django.db.models import Q
from django.contrib.postgres.search import SearchVector

from .models import Country, State, Place

class SearchResultsView(ListView):
    model = Place  # for example
    template_name = 'search_results.html'

    def get_queryset(self):
        query = self.request.GET.get('q')
        return Place.objects.annotate(
            search=SearchVector('name', 'state__name', 'state__country__name'),
        ).filter(search=query)

