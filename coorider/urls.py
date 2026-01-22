from django.urls import path
from . import views

urlpatterns = [
    # Web pages
    path('', views.dashboard, name='dashboard'),          # Dashboard page
    path('login/', views.login_view, name='login'),       # Animal login page
    path('sensor/', views.sensor_view, name='sensor'),    # Animal GPS page

    # API endpoints for live tracking
    path('api/update-location/', views.update_location, name='update_location'),  # POST from animal phone
    path('api/get-locations/', views.get_locations, name='get_locations'),        # GET all animal locations
]
