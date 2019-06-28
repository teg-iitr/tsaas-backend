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

class TripModeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mode
        fields = (
            'modeID',
            'modeType',
            'accessMode',
            'cost',
            'fare',
            'travelDistance',
            'travelTime'
        )

class TripODSerializer(serializers.ModelSerializer):
    class Meta:
        model = OriginDestination
        fields = (
            'originDestinationID',
            'originPlace',
            'originLat',
            'originLng',
            'destinationPlace',
            'destinationLat',
            'destinationLng',
        )

class TripODModeSerializer(serializers.ModelSerializer):
    origin_destination = TripODSerializer(many=True)
    mode_types = TripModeSerializer(many=True)

    class Meta:
        model = Trip
        fields = (
            'tripID',
            'origin_destination',
            'mode_types',
        )


class MemberTripSerializer(serializers.ModelSerializer):
    trips = TripODModeSerializer(many=True)

    class Meta:
        model = Member
        fields = (
            'memberID',
            'created_at',
            'gender',
            'age',
            'educationalQualification',
            'monthlyIncome',
            'maritialStatus',
            'differentlyAbled',
            'homeState',
            'nameOfDistrict',
            'landmark',
            'pincode',
            'principalSourceofIncome',
            'lat',
            'lng',
            'tripsMade',
            'trips'
        )


class FamilyMemberSerializer(serializers.ModelSerializer):
    members = MemberTripSerializer(many = True)

    class Meta:
        model = Family
        fields = (
            'familyID',
            'noOfCars',
            'noOfCycles',
            'noOfTwoWheelers',
            'familyIncome',
            'members',
        )

class ViewAllSerializer(serializers.ModelSerializer):
    # College = CollegeListSerializer()
    # college = serializers.PrimaryKeyRelatedField(
    #     queryset=Family.objects.all(),
    #     many=True,
    # )
    families = FamilyMemberSerializer(many=True)
    # Member = MemberSerializer(many=True)
    # Trip = TripSerializer(many=True)
    # OriginDestination = OriginDestinationSerializer(many=True)
    # Mode = ModeSerializer(many=True)

    class Meta:
        model = CollegeList
        fields = (
            'collegeName',
            'families'
            )
        # fields = '__all__'