import uuid
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import get_user_model
from ..serializers import UserSerializer


User = get_user_model()

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    
    
    
    def get_permissions(self):
            if self.action == 'create':
                # Si la accion es crear, no se requiere autenticacion
                return [AllowAny()]
            return [IsAuthenticated()] 
        
    def create(self, request, *args, **kwargs):
        
        # Validadmos los datos con el serializador (que solo expone o valida campos)
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.validated_data
        
        # Si no viene el 'username' requerido por el system, lo creamos
        if not data.get('username'):
            local = data['email'].split('@')[0]
            data['username'] = f"{local}-{uuid.uuid4().hex[:6]}"
        
        
        # Creamos el usuario con el create_user() para que el password se hashee
        user = User.objects.create_user(**serializer.validated_data)
        
        # Si el usuario se crea correctamente, generamos un token de acceso
        refresh = RefreshToken.for_user(user)
        access = refresh.access_token
        
        
        # Serializamos el usuario creado (para la respuesta)
        out_serializer = self.get_serializer(user)
        
        # Construimos la respueta a medida
        response_data = {
            'user': out_serializer.data,
            'tokens': {
                'refreshToken': str(refresh),
                'accessToken': str(access),
            },
            # 'status': 'success',
            'message': 'Usuario creado correctamente',
        }
        
        # Construimos la respuesta  en codigo 201 y headers de creacion
        headers = self.get_success_headers(out_serializer.data)
        return Response(response_data, status=status.HTTP_201_CREATED, headers=headers)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
#    def update(self, request, *args, **kwargs):
    #     """
    #     Si quieres permitir que en PUT/PATCH también se cambie la contraseña y se hashee,
    #     podrías hacer algo similar aquí detectando 'password' en request.data.
    #     """
    #     partial = kwargs.pop('partial', False)
    #     instance = self.get_object()
    #     serializer = self.get_serializer(instance, data=request.data, partial=partial)
    #     serializer.is_valid(raise_exception=True)

    #     pwd = serializer.validated_data.pop('password', None)
    #     for attr, value in serializer.validated_data.items():
    #         setattr(instance, attr, value)
    #     if pwd:
    #         instance.set_password(pwd)
    #     instance.save()

    #     return Response(self.get_serializer(instance).data)