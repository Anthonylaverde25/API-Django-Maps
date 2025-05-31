from django.db import models
from django.conf import settings
from accounts.validators import handle_validator

class Profile(models.Model):
    '''
    Model to store public profile information of the user.
    It is associated one-to-one with CustomUser.
    '''
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='profile'
    )
    
    # Public handle (unique user alias)
    handle = models.CharField(
        max_length=30,
        unique=True,
        blank=False,
        validators=[handle_validator],
        help_text="Public alias (letters, numbers, _ and -; 3-30 characters)"
    )
    
    # Initials of the user's first and last name (required)
    siglas = models.CharField(
        max_length=2,
        blank=False,
        help_text="Initials of the user's first and last name (required)"
    )
    
    bio = models.CharField(
        max_length=160,
        blank=True,
        help_text='A short bio or description about yourself'
    )
    
    # Optional contact phone number
    phone = models.CharField(
        max_length=20,
        blank=True,
        null=True,
        help_text="Optional contact phone number"
    )
    
    image = models.ImageField(
        upload_to='profile_images/',
        blank=True,
        null=True,
        help_text='Profile image'
    )
