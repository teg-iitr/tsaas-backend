from rest_framework import serializers
from transdb.models import Family, Member, Trip, OriginDestination, Mode

# For converting JSON data to models

class FamilySerializer(serializers.ModelSerializer):
    class Meta:
        model = Family
        fields = '__all__'

class MemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Member
        fields = '__all__'

class TripSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trip
        fields = '__all__'

class OriginDestinationSerializer(serializers.ModelSerializer):
    class Meta:
        model = OriginDestination
        fields = '__all__'

class ModeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mode
        fields = '__all__'        