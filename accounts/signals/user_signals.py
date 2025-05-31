
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings
from ..models.profile import Profile


def generate_siglas(user):
    """Genera las siglas usando la primera letra del nombre y apellido."""
    siglas= ""
    if user.first_name and user.last_name:
        siglas = user.first_name[0].upper() + user.last_name[0].upper()
        return siglas
    
    

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_or_update_profile(sender, instance, created, **kwargs):
    if created:
        # Si el perfil no existe, lo creamos y usamos la funcion generate_siglas
        handle = f"user_{instance.id}"
        Profile.objects.create(user=instance, siglas=generate_siglas(instance), handle=handle)
        
    else:
        #si el perfil ya existe, lo actualizamos
        try:
            profile = instance.profile
            new_initial = generate_siglas(instance)
            
            if profile.siglas != new_initial:
                profile.siglas = new_initial
                profile.save(update_fields=["siglas"])
                
        except Profile.DoesNotExist:
            # Si el perfil no existe, lo creamos
            Profile.objects.create(user=instance, siglas=generate_siglas(instance))
        





