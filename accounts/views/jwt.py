from rest_framework_simplejwt.views import TokenObtainPairView
from accounts.serializers.jwt import CustomTokenObtainPairSerializer

class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer
