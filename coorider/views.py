from django.shortcuts import render
from django.http import JsonResponse
import json

# Store animal locations in memory (demo purposes)
ANIMAL_LOCATIONS = {}

# ---------------------
# Dashboard page
# ---------------------
def dashboard(request):
    return render(request, 'index.html')

# ---------------------
# Animal login page
# ---------------------
def login_view(request):
    error = None
    if request.method == 'POST':
        animal_id = request.POST.get('animal_id')
        if animal_id:
            return render(request, 'sensor.html', {'animal_id': animal_id})
        else:
            error = "Please enter Animal ID."
    return render(request, 'login.html', {'error': error})

# ---------------------
# Animal sensor page
# ---------------------
def sensor_view(request):
    return render(request, 'sensor.html')

# ---------------------
# API: Update animal GPS
# ---------------------
def update_location(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            animal_id = data.get('animal_id')
            lat = data.get('latitude')
            lng = data.get('longitude')
            if animal_id and lat and lng:
                ANIMAL_LOCATIONS[animal_id] = {'latitude': lat, 'longitude': lng}
                return JsonResponse({'status': 'ok'})
            else:
                return JsonResponse({'error': 'Invalid data'}, status=400)
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON'}, status=400)
    return JsonResponse({'error': 'Invalid method'}, status=400)

# ---------------------
# API: Get all animal locations
# ---------------------
def get_locations(request):
    response = []
    for animal_id, loc in ANIMAL_LOCATIONS.items():
        response.append({
            'animal_id': animal_id,
            'latitude': loc['latitude'],
            'longitude': loc['longitude']
        })
    return JsonResponse(response, safe=False)
