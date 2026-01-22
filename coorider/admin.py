from django.contrib import admin
from .models import AnimalLocation

@admin.register(AnimalLocation)
class AnimalLocationAdmin(admin.ModelAdmin):
    list_display = ('animal_id', 'latitude', 'longitude', 'timestamp')
    list_filter = ('animal_id',)
    search_fields = ('animal_id',)

