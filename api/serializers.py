from rest_framework import serializers
from .models import cook

class cookSerializer(serializers.ModelSerializer):
    class Meta:
        model = cook
        fields = ['id', 'name', 'created_at', 'updated_at']
