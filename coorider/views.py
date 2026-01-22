from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import AnimalLocation
import json


def dashboard(request):
    """
    Admin dashboard – shows map
    """
    return render(request, 'dashboard.html')


@csrf_exempt
def update_location(request):
    """
    API endpoint
    Phone (animal) sends GPS location here
    """
    if request.method == 'POST':
        data = json.loads(request.body)

        animal_id = data.get('animal_id')
        latitude = data.get('latitude')
        longitude = data.get('longitude')

        AnimalLocation.objects.update_or_create(
            animal_id=animal_id,
            defaults={
                'latitude': latitude,
                'longitude': longitude
            }
        )

        return JsonResponse({'status': 'success'})

    return JsonResponse({'error': 'Invalid request'}, status=400)


def get_locations(request):
    """
    Sends all animal locations to map
    """
    locations = AnimalLocation.objects.all()
    data = []

    for loc in locations:
        data.append({
            'animal_id': loc.animal_id,
            'latitude': loc.latitude,
            'longitude': loc.longitude
        })

    return JsonResponse(data, safe=False)

