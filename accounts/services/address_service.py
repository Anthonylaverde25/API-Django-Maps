# accounts/services/address_service.py
from ..utils.geolocation import geocode_address
from django.db import transaction
from django.shortcuts import get_object_or_404
from accounts.models import Address, logEntry

class AddressService:
    @staticmethod
    @transaction.atomic
    def sync_addresses_for_profile(profile, addresses_data):
        """
        Sincroniza las direcciones de un Profile:
         1) Borrar las que el profile ya tenía pero cuyo 'id' no viene en addresses_data.
         2) Para cada dict en addresses_data:
            - Si trae 'id', actualiza esa Address.
            - Si no trae 'id', crea una nueva asociada al profile.
        """
        # 1) Extraer IDs entrantes
        incoming_ids = {
            addr.get('id') for addr in addresses_data
            if addr.get('id') is not None
        }

        # 2) Borrar las direcciones que ya no vienen en el payload
        # se genera un queryset de direcciones que no etan en el payload
        # se eliminan todas las instancias que no correspoden
        profile.addresses.exclude(id__in=incoming_ids).delete()

        # 3) Recorrer payload y update/create
        for raw in addresses_data:
            data = raw.copy()  # evita mutar raw
            addr_id = data.pop('id', None)
            
            #Geodecode, implementaremos el metodo para obtener cordenadas
            location = geocode_address(
                data.get('country', ''),
                data.get('state', ''),
                data.get('city', ''),
                data.get('street', ''),
                data.get('postal_code', ''),
            )

            if addr_id:
                # UPDATE: traemos la instancia, reasignamos campos y salvamos
                addr_obj = get_object_or_404(Address, id=addr_id, profile=profile)
                for field, value in data.items():
                    setattr(addr_obj, field, value)
                if location:
                    addr_obj.location = location
                addr_obj.save()
            else:
                # CREATE
                if location:
                    data['location'] = location
                Address.objects.create(profile=profile, **data)
    
    
    
    @staticmethod
    @transaction.atomic
    def sync_address_add_for_logEntry(data):
        
        country, state, city, street, postal_code = (data.get(k, "") for k in ("country", "state", "city", "street", "postal_code"))
        location = geocode_address(country, state, city, street, postal_code)
        
        if location:
            data['location'] = location
        return data
            
            
        
        
        
