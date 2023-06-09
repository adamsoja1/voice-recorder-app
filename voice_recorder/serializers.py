from .models import Record
from rest_framework import serializers



class RecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = Record
        fields = ('id','date', 'audio_file')

