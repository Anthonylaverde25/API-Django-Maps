from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from django.contrib.gis.geos import Point
from django.db import transaction
from accounts.models import Profile, Address


class Command(BaseCommand):
    help = 'Creates an initial user, profile and one address using PostGIS PointField.'

    def add_arguments(self, parser):
        parser.add_argument('--email',       type=str,   default='super_admin@example.com',
                            help='Email for the new user')
        parser.add_argument('--username',    type=str,   default='test_user',
                            help='Username (required by AbstractUser)')
        parser.add_argument('--password',    type=str,   default='123456789',
                            help='Password for the new user')
        parser.add_argument('--handle',      type=str,   default='superadmin_alias',
                            help='Unique public alias for the profile')
        parser.add_argument('--siglas',      type=str,   default='SA',
                            help='Initials (2 characters)')
        parser.add_argument('--phone',       type=str,   default='',
                            help='Optional phone number')
        parser.add_argument('--country',     type=str,   default='Argentina',
                            help='Country for the address')
        parser.add_argument('--city',        type=str,   default='Buenos Aires',
                            help='City for the address')
        parser.add_argument('--street',      type=str,   default='Av. Siempre Viva 742',
                            help='Street address')
        parser.add_argument('--postal_code', type=str,   default='C1000AAA',
                            help='Postal code')
        parser.add_argument('--lat',         type=float, default=-34.603722,
                            help='Latitude for the PointField (ej: -34.603722)')
        parser.add_argument('--lon',         type=float, default=-58.381570,
                            help='Longitude for the PointField (ej: -58.381570)')

    def handle(self, *args, **options):
        User = get_user_model()
        email       = options['email']
        username    = options['username']
        password    = options['password']
        handle      = options['handle']
        siglas      = options['siglas']
        phone       = options['phone']
        country     = options['country']
        city        = options['city']
        street      = options['street']
        postal_code = options['postal_code']
        lat         = options['lat']
        lon         = options['lon']

        with transaction.atomic():
            # 1) Crear o recuperar el usuario
            user, created_u = User.objects.get_or_create(
                email=email,
                defaults={'username': username}
            )
            if created_u:
                user.set_password(password)
                user.save()
                self.stdout.write(self.style.SUCCESS(f'✔ Usuario creado: {email}'))
            else:
                self.stdout.write(self.style.WARNING(f'ℹ Usuario ya existe: {email}'))

            # 2) Crear o recuperar el profile
            profile, created_p = Profile.objects.get_or_create(
                user=user,
                defaults={'handle': handle, 'siglas': siglas, 'phone': phone}
            )
            if created_p:
                self.stdout.write(self.style.SUCCESS(f'✔ Profile creado para {email}'))
            else:
                self.stdout.write(self.style.WARNING(f'ℹ Profile ya existe para {email}'))

            # 3) Crear la dirección
            point = Point(lon, lat)  # GEOS espera (x=lon, y=lat)
            address = Address.objects.create(
                profile=profile,
                country=country,
                city=city,
                street=street,
                postal_code=postal_code,
                location=point
            )
            self.stdout.write(self.style.SUCCESS(f'✔ Address creada: {address}'))
