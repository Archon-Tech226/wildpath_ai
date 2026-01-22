
from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),                 # Laptop dashboard
    path('api/update-location/', views.update_location, name='update_location'),  # Phone sends GPS
    path('api/get-locations/', views.get_locations, name='get_locations'),        # Laptop fetches live data
]
