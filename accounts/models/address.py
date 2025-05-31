from django.contrib.gis.db import models  # Esto importa el módulo de GIS
from .profile import Profile

class Address(models.Model):
    profile = models.ForeignKey(
        Profile, related_name='addresses',
        on_delete=models.CASCADE,
    )
    country = models.CharField(max_length=100)
    state = models.CharField(max_length=100, blank=True, null=True)
    city = models.CharField(max_length=100)
    street = models.CharField(max_length=255)
    postal_code = models.CharField(max_length=20)
    location = models.PointField(null=True, blank=True)  # Geoespacial
    
    def __str__(self):
      return f'{self.street}, {self.city}, {self.country}'


    