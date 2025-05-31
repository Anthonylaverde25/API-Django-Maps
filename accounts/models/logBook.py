

# Importamos el modulo de modelos de Django con soporte GIS. Se emplea igual que dejango.db.models
# pero permite campos geoespaciales
from django.contrib.gis.db import models
from .profile import Profile

class LogBook(models.Model):
    
    # Creamos un campo de clave foranea apuntando al modelo Profile  
    profile = models.ForeignKey(
        # El related name nos permite acceder acceder desde un perfil a su relacion con este modelo
        # por ejemplo, my_profile.logbooks.all()
        Profile, related_name='logbooks',
        
        # Si borramos un profile, se borra en cascada todas sus relaciones con este modelo
        on_delete=models.CASCADE
    )
    
    entries = models.ManyToManyField(
        'LogEntry',
        related_name='logbooks',
        blank=True
    )
    
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    
    class Meta:
        verbose_name = 'Logbook'
        verbose_name_plural = 'Logbooks'
        
    def __str__(self):
        return f'{self.title} ({self.profile.user.username})'


