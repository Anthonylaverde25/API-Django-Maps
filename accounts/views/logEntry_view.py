from accounts.models import LogEntry
from accounts.serializers import LogEntrySerializer
from accounts.services.address_service import AddressService
from rest_framework import viewsets, permissions
from rest_framework.response import Response

class LogEntryViewSet(viewsets.ModelViewSet):
    queryset = LogEntry.objects.all()
    serializer_class = LogEntrySerializer
    permission_classes = [permissions.IsAuthenticated]
    
    
    def create(self, request, *args, **kwargs):
        data = request.data.copy()
        enriched_data = AddressService.sync_address_add_for_logEntry(data)

        serializer = self.get_serializer(data = enriched_data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(serializer.data, status=201)
    
        
        
        
        
        
        
        
