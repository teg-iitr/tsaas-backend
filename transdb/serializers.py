from rest_framework import serializers
from transdb.models import Family, Member, Trip, OriginDestination, Mode, CollegeList

# For converting JSON data to models

class CollegeListSerializer(serializers.ModelSerializer):
    class Meta:
        model = CollegeList
        fields = '__all__'

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

class ViewAllSerializer(serializers.ModelSerializer):
    # Family = FamilySerializer(read_only=True)
    familyID = serializers.RelatedField(read_only=True, many=True)
    # Trip = TripSerializer(read_only=True)
    # OriginDestination = OriginDestinationSerializer(read_only=True)
    # Mode = ModeSerializer(read_only=True)

    class Meta:
        model = Family
        fields = '__all__'