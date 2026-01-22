from django.db import models

class AnimalLocation(models.Model):
    animal_id = models.CharField(max_length=50)
    latitude = models.FloatField()
    longitude = models.FloatField()
    timestamp = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.animal_id} @ ({self.latitude}, {self.longitude})"

