from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    
    USERNAME_FIELD = 'email' # Usamos el email como el campo principal de autenticacion
    REQUIRED_FIELDS = ['username']  # `username` sigue siendo necesario para el createsuperuser, pero no es el campo de autenticación

    