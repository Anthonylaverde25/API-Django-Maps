from accounts.models import LogBook
from accounts.serializers import LogBookSerializer
from rest_framework import viewsets, permissions
from rest_framework.response import Response


class LogBookViewSet(viewsets.ModelViewSet):
    # Esto es un ViewSet, le dice a DRF que conjunto de objectos
    # de base de datos debe exponer y manejar el endpoint, en este caso tenemos que
    # LogBook.objects es un manager. a traves de el se llaman metodo como los api rest
    # .all() implica recuperar todas las instancias
    queryset = LogBook.objects.all()
    serializer_class = LogBookSerializer
    permission_classes = [permissions.IsAuthenticated]