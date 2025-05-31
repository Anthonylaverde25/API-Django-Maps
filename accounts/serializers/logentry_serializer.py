
from accounts.models import LogEntry, LogBook
from rest_framework import serializers

class LogEntrySerializer(serializers.ModelSerializer):
    # Campo para recibir los IDs de los LogBooks relacionados
    logbooks = serializers.PrimaryKeyRelatedField(
        many=True,
        queryset=LogBook.objects.all(),
        required=False
    )

    class Meta:
        model = LogEntry
        fields = '__all__'
        read_only_fields = ('id', 'timestamp')

    def create(self, validated_data):
        # Sacamos los logbooks para manejar la relación después
        logbooks = validated_data.pop('logbooks', [])
        # Creamos la instancia LogEntry sin logbooks
        logentry = LogEntry.objects.create(**validated_data)
        # Añadimos la relación en el lado de LogBook
        for logbook in logbooks:
            logbook.entries.add(logentry)
        return logentry
