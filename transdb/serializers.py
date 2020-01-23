from rest_framework import serializers
from transdb.models import (
    Family,
    Member,
    Trip,
    OriginDestination,
    Mode,
    CollegeList,
    Feedback,
    MemberDistrict,
    SurveyList,
    ResponseTime,
    SurveyType,
    PtSurvey,
    PtSurveyRating
    )

from django.db.models import Q
from django.contrib.auth import get_user_model

# For converting JSON data to models

class TypeSerialiazer(serializers.ModelSerializer):
    class Meta:
        model = SurveyType
        fields = '__all__'

class SurveyListSerializer(serializers.ModelSerializer):
    class Meta:
        model = SurveyList
        fields = '__all__'

class ResponseTimeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ResponseTime
        fields = '__all__'

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

class MemberDistrictSerializer(serializers.ModelSerializer):
    class Meta:
        model = MemberDistrict
        fields = '__all__'

class OriginDestinationSerializer(serializers.ModelSerializer):
    class Meta:
        model = OriginDestination
        fields = '__all__'

class ModeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mode
        fields = '__all__'

class FeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feedback
        fields = '__all__'

class PtSurveySerializer(serializers.ModelSerializer):
    class Meta:
        model = PtSurvey
        fields = '__all__'

class PtSurveyRatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = PtSurveyRating
        fields ='__all__'

class TripModeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mode
        fields = (
            'modeID',
            'modeName',
            'modeIndex',
        )

class TripODSerializer(serializers.ModelSerializer):
    class Meta:
        model = OriginDestination
        fields = (
            'originDestinationID',
            'originLandmark',
            'originPlace',
            'originLat',
            'originLng',
            'destinationLandmark',
            'destinationPlace',
            'destinationLat',
            'destinationLng',
            'fare',
            'travelDistance',
            # 'travelTime'
            'departureTime',
            'arrivalTime'
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
            'principalSourceofIncome',
            'stayAtHome',
            'householdHead',
            'respondent',
            'twoWheelerLicense',
            'simCards',
            'fourWheelerLicense',
            'dataWhileDriving',
            'bluetooth',
            'wifi',
            'trips',
            'district'
        )


class FamilyMemberSerializer(serializers.ModelSerializer):
    members = MemberTripSerializer(many = True)

    class Meta:
        model = Family
        fields = (
            'familyID',
            'noOfMembers',
            'noOfCars',
            'noOfCycles',
            'noOfTwoWheelers',
            'familyIncome',
            'country',
            'homeState',
            'nameOfDistrict',
            'landmark',
            'lat',
            'lng',
            'members',
        )

class ViewAllSerializer(serializers.ModelSerializer):
    families = FamilyMemberSerializer(many=True)


    class Meta:
        model = CollegeList
        fields = (
            'collegeURL',
            'collegeName',
            'families'
            )
