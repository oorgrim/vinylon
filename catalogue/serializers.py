from rest_framework import serializers
from .models import VinylRecord

class VinylRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = VinylRecord
        fields = '__all__ '