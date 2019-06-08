from rest_framework import serializers
from transdb.models import TransDB

# For converting JSON data to models

class TransDBSerializer(serializers.ModelSerializer):
    class Meta:
        model = TransDB
        fields = '__all__'