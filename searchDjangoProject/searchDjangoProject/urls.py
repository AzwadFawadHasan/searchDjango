from django.contrib import admin
from django.urls import path, include
from locations.views import SearchResultsView
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('search/', SearchResultsView.as_view(), name='search_results'),
    path('', include('locations.urls')),  # This assumes you have URLs defined in your locations app
    
]
