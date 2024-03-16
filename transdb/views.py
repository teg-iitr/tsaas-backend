from django.shortcuts import render

# Create your views here.
from transdb.models import Family, Member, Trip, OriginDestination, Mode, CollegeList
from transdb.serializers import FamilySerializer, MemberSerializer, TripSerializer, OriginDestinationSerializer, ModeSerializer, CollegeListSerializer
from rest_framework import viewsets


class CollegeListCreate(viewsets.ModelViewSet):
    queryset = CollegeList.objects.all()
    serializer_class = CollegeListSerializer


class FamilyListCreate(viewsets.ModelViewSet):
    queryset = Family.objects.all()
    serializer_class = MemberSerializer


class MemberListCreate(viewsets.ModelViewSet):
    queryset = Member.objects.all()
    serializer_class = MemberSerializer


class TripListCreate(viewsets.ModelViewSet):
    queryset = Trip.objects.all()
    serializer_class = MemberSerializer


class OriginDestinationListCreate(viewsets.ModelViewSet):
    queryset = OriginDestination.objects.all()
    serializer_class = MemberSerializer


class ModeListCreate(viewsets.ModelViewSet):
    queryset = Mode.objects.all()
    serializer_class = MemberSerializer
