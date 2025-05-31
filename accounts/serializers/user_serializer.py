from django.contrib.auth import get_user_model
from rest_framework import serializers

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, min_length=8, help_text="La contraseña debe tener al menos 8 caracteres.")
    
    username = serializers.CharField(
      required=False,
      allow_blank=True,
        help_text="El nombre de usuario es opcional, pero si se proporciona, debe ser único."  
    )
    
    class Meta:
        model = User
        fields = ['id','first_name', 'last_name', 'email', 'password', 'username']
        