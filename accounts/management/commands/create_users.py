from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from django.contrib.gis.geos import Point
from django.db import transaction
from accounts.models import Profile, Address

class Command(BaseCommand):
    help = 'Crea 3 usuarios (con eliminación previa si ya existen), perfiles y direcciones.'

    def handle(self, *args, **options):
        User = get_user_model()

        users_data = [
            {
                'email': 'lucia.gonzalez@example.com',
                'username': 'lucia_gonzalez',
                'first_name': 'Lucía',
                'last_name': 'González',
                'handle': 'luciaG',
                'siglas': 'LG',
                'bio': '✨ Amante de los libros 📚 y el café ☕. Siempre aprendiendo algo nuevo. #Desarrollo 💻',
                'addresses': [
                    {
                        'city': 'Buenos Aires',
                        'street': 'Av. Corrientes 123',
                        'lat': -34.603722,
                        'lon': -58.381570
                    }
                ]
            },
            {
                'email': 'martin.perez@example.com',
                'username': 'martin_perez',
                'first_name': 'Martín',
                'last_name': 'Pérez',
                'handle': 'martinP',
                'siglas': 'MP',
                'bio': '🚴‍♂️ Apasionado por el ciclismo y las aventuras al aire libre 🌍. Siempre buscando nuevos retos! 💪',
                'addresses': [
                    {
                        'city': 'Mar del Plata',
                        'street': 'Calle Güemes 456',
                        'lat': -38.005477,
                        'lon': -57.542610
                    }
                ]
            },
            {
                'email': 'sofia.ramirez@example.com',
                'username': 'sofia_ramirez',
                'first_name': 'Sofía',
                'last_name': 'Ramírez',
                'handle': 'sofiaR',
                'siglas': 'SR',
                'bio': '🎨 Artista digital 🖌️ y fotógrafa 📸. Aquí para compartir mi pasión por el arte y la creatividad ✨',
                'addresses': [
                    {
                        'city': 'Buenos Aires',
                        'street': 'Av. Santa Fe 789',
                        'lat': -34.591556,
                        'lon': -58.397325
                    },
                    {
                        'city': 'Mar del Plata',
                        'street': 'Calle Olavarría 321',
                        'lat': -38.003501,
                        'lon': -57.538198
                    }
                ]
            }
        ]

        password = '123456789'
        country = 'Argentina'
        postal_code = 'B0000AAA'

        for u in users_data:
            with transaction.atomic():
                existing_user = User.objects.filter(email=u['email']).first()
                if existing_user:
                    self.stdout.write(self.style.WARNING(f'⚠ Eliminando usuario existente: {u["email"]}'))
                    existing_user.delete()

                # Crear nuevo usuario
                user = User.objects.create_user(
                    email=u['email'],
                    username=u['username'],
                    first_name=u['first_name'],
                    last_name=u['last_name'],
                    password=password
                )
                self.stdout.write(self.style.SUCCESS(f'✔ Usuario creado: {user.email}'))

                # Crear nuevo perfil
                profile = Profile.objects.create(
                    user=user,
                    handle=u['handle'],
                    siglas=u['siglas'],
                    phone='',
                    bio=u.get('bio', '')  # Establecer bio con un valor por defecto si no está presente
                )
                self.stdout.write(self.style.SUCCESS(f'✔ Profile creado para {user.email}'))

                # Crear direcciones
                for addr in u['addresses']:
                    location = Point(addr['lon'], addr['lat'])  # lon = x, lat = y
                    address = Address.objects.create(
                        profile=profile,
                        country=country,
                        city=addr['city'],
                        street=addr['street'],
                        postal_code=postal_code,
                        location=location
                    )
                    self.stdout.write(self.style.SUCCESS(f'✔ Dirección creada: {address}'))
