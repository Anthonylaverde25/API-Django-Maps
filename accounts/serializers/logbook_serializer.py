from accounts.models import LogBook
from rest_framework import serializers

class LogBookSerializer(serializers.ModelSerializer):
    class Meta:
        model = LogBook
        fields = '__all__'