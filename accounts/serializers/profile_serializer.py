from rest_framework import serializers
from accounts.models import Profile
# from accounts.serializers import AddressSerializer, UserSerializer
from .address_serializer import AddressSerializer
from .user_serializer import UserSerializer

class ProfileSerializer(serializers.ModelSerializer):
    addresses = AddressSerializer(many=True, read_only=True)
    user = UserSerializer(read_only=True)
    class Meta:
        model = Profile
        fields = ['id', 'user', 'handle', 'siglas', 'phone', 'addresses', 'bio', 'image']
        read_only_fields = ['user']  # si el user lo asignas automáticamente

