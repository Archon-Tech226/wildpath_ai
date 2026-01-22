// Initialize map
var map = L.map('map').setView([11.0, 76.9], 12);  // Center coordinates

// Load OpenStreetMap tiles
L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    maxZoom: 19
}).addTo(map);

// Keep track of animal markers
var markers = {};

// Fetch animal locations every 3 seconds
setInterval(function() {
    fetch('/api/get-locations/')
        .then(response => response.json())
        .then(data => {
            data.forEach(a => {
                if (markers[a.animal_id]) {
                    // Move existing marker
                    markers[a.animal_id].setLatLng([a.latitude, a.longitude])
                                         .bindPopup(a.animal_id);
                } else {
                    // Create new marker
                    markers[a.animal_id] = L.marker([a.latitude, a.longitude])
                                             .addTo(map)
                                             .bindPopup(a.animal_id);
                }
            });
        })
        .catch(err => console.error("Error fetching locations:", err));
}, 3000);

