from transdb.models import (
    Family,
    Member,
    Trip,
    OriginDestination,
    Mode,
    CollegeList,
    Feedback
    )
from rest_framework import viewsets, permissions, status
from .serializers import (
    FamilySerializer,
    MemberSerializer,
    TripSerializer,
    OriginDestinationSerializer,
    ModeSerializer,
    ViewAllSerializer,
    CollegeListSerializer,
    FeedbackSerializer
    )
from rest_framework.response import Response
# from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAdminUser

# TransDB viewset

class CollegeListViewSet(viewsets.ViewSet):
    queryset = CollegeList.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = CollegeListSerializer

    def list(self, request, *args, **kwargs):
        queryset = CollegeList.objects.all()
        serializer = CollegeListSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class FamilyViewSet(viewsets.ViewSet):
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

class MemberViewSet(viewsets.ViewSet):
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

class TripViewSet(viewsets.ViewSet):
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

class OriginDestinationViewSet(viewsets.ViewSet):
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


class ModeViewSet(viewsets.ViewSet):
    queryset = Mode.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = ModeSerializer

    def create(self, request, *args, **kwargs):
        serializer = ModeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class FeedbackViewSet(viewsets.ViewSet):
    queryset = Feedback.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = FeedbackSerializer

    def create(self, request, *args, **kwargs):
        serializer = FeedbackSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ViewAllViewSet(viewsets.ViewSet):
    # authentication_classes = [SessionAuthentication, BasicAuthentication]

    # permission_classes = [IsAuthenticated, IsAdminUser]
    permission_classes = [permissions.AllowAny]
    # permission_classes = [IsAdminUser]

    def list(self, request):
        queryset = CollegeList.objects.all()
        serializer = ViewAllSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
