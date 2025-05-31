from rest_framework import viewsets, permissions
from rest_framework.response import Response  # Correcta importación de Response
from rest_framework.decorators import action
from accounts.models import Profile
from accounts.serializers import ProfileSerializer
from accounts.services.address_service import AddressService

class ProfileViewSet(viewsets.ModelViewSet):
    queryset = (
        Profile.objects
            .select_related('user').prefetch_related('addresses').all()
    )
    
    serializer_class = ProfileSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    @action(detail=False, methods=['get'], permission_classes=[permissions.IsAuthenticated])
    def me(self, request):
        profile = Profile.objects.select_related('user').prefetch_related('addresses').get(user=request.user)
        serializer = self.get_serializer(profile)
        return Response({'auth_profile': serializer.data})  # Aquí usamos Response correctamente

    def perform_update(self, serializer):
        # Guardamos los cambios basicos del profile
        profile = serializer.save()
        
        # Extraemos el array de direcciones (puede venir vacio)
        addresses_data = self.request.data.get('addresses', [])
        
        # Llamamos al servicio que actualiza/crea/borrar direciones
        AddressService.sync_addresses_for_profile(profile, addresses_data)
        