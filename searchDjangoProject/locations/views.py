from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .models import Place

from django.shortcuts import render
from .models import Place

from django.db.models import Q

def search(request):
    query = request.GET.get('q', '')
    places = []

    if query:
        places = Place.objects.filter(Q(name__icontains=query) | Q(state__name__icontains=query))

    return render(request, 'search.html', {'places': places, 'query': query})


from django.http import JsonResponse

def autocomplete(request):
    query = request.GET.get('q', '')
    places = Place.objects.filter(name__icontains=query).values_list('name', flat=True)
    return JsonResponse(list(places), safe=False)
