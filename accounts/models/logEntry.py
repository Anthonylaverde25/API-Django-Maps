from django.contrib.gis.db import models
from .logBook import LogBook

class LogEntry(models.Model):
    title       = models.CharField(max_length=200)
    description = models.TextField(blank=True)

    # Marca de tiempo de la entrada
    timestamp   = models.DateTimeField(auto_now_add=True)

    # Campos de ubicación específicos de este punto de interés
    country     = models.CharField(max_length=100)
    state       = models.CharField(max_length=100, blank=True, null=True)
    city        = models.CharField(max_length=100)
    street      = models.CharField(max_length=255)
    postal_code = models.CharField(max_length=20)

    # Coordenadas geoespaciales (lat/lng)
    location    = models.PointField(null=True, blank=True)

    class Meta:
        verbose_name        = 'Log Entry'
        verbose_name_plural = 'Log Entries'
        ordering            = ['-timestamp']

    def __str__(self):
        return f'{self.title} @ {self.timestamp:%Y-%m-%d %H:%M}'
