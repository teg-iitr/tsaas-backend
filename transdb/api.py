from transdb.models import Family, Member, Trip, OriginDestination, Mode
from rest_framework import viewsets, permissions, status
from .serializers import FamilySerializer, MemberSerializer, TripSerializer, OriginDestinationSerializer, ModeSerializer,ViewAllSerializer
from rest_framework.response import Response

# TransDB viewset
class FamilyViewSet(viewsets.ModelViewSet):
    queryset = Family.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = FamilySerializer

    def create(self, request, *args, **kwargs):
        try:
            family_id = Family.objects.all().last().familyID+1
        except:
            family_id = 1
        data = {'familyID':family_id}
        serializer = FamilySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # def list(self, request, *args, **kwargs):
        # return Response({'something': 'my custom JSON'})

class MemberViewSet(viewsets.ModelViewSet):
    queryset = Member.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = MemberSerializer

    def create(self, request, *args, **kwargs):
        serializer = MemberSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class TripViewSet(viewsets.ModelViewSet):
    queryset = Trip.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = TripSerializer

    def create(self, request, *args, **kwargs):
        serializer = TripSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class OriginDestinationViewSet(viewsets.ModelViewSet):
    queryset = OriginDestination.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = OriginDestinationSerializer

    def create(self, request, *args, **kwargs):
        serializer = OriginDestinationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ModeViewSet(viewsets.ModelViewSet):
    queryset = Mode.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = ModeSerializer

class ViewAllViewSet(viewsets.ModelViewSet):
    queryset = Family.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = ViewAllSerializer