from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .models import Place

def search(request):
    query = request.GET.get('q', '')
    places = Place.objects.filter(name__icontains=query)
    return render(request, 'search.html', {'places': places, 'query': query})
