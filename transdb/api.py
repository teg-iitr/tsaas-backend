import pandas as pd
import random
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
    PtSurveyRating,
    AQIPerceptionSurvey,
    TabletravelDetalis,
    IndoreStopsList
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
    FeedbackSerializer,
    MemberDistrictSerializer,
    SurveyListSerializer,
    ResponseTimeSerializer,
    TypeSerialiazer,
    PtSurveySerializer,
    PtSurveyRatingSerializer,
    AQIPerceptionSurveySerializer,
    TabletravelDetalisSerialiazer,
    TableWillingnessSurveyDetails,
    IndoreStopsListSerializer

)

from pathlib import Path
import pandas as pd
from rest_framework.response import Response
# from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAdminUser, AllowAny

from rest_framework import generics, mixins, views
from django.shortcuts import get_object_or_404

# reading the csv file for the indore from local system


class ReadWillingnessData(viewsets.ViewSet):
    permission_classes = [AllowAny]

    def list(self, request, *args, **kwargs):
        filename = r'C:\Users\manis\Downloads\optimal_design.csv'
        filename = Path(filename)
        df = pd.read_csv(filename)  # Read CSV file
        for index, row in df.iterrows():
            print(f'Row {index}:')
            print(row['alt1_TravelTime'])
            table_details = TabletravelDetalis(
                alt1_TravelTime=row['alt1_TravelTime'],
                alt1_TravelCost=row['alt1_TravelCost'],
                alt1_Standing=row['alt1_Standing'],
                alt1_Crowding=row['alt1_Crowding'],
                alt2_TravelTime=row['alt2_TravelTime'],
                alt2_TravelCost=row['alt2_TravelCost'],
                alt2_Standing=row['alt2_Standing'],
                alt2_Crowding=row['alt2_Crowding'],
                used=0,
                table_used_number=row['Block']
            )
            # Save the instance to the database
            table_details.save()

        return Response(df.to_dict(orient='records'), status=status.HTTP_201_CREATED)


class ReadIndoreCsv(viewsets.ViewSet):
    permission_classes = [AllowAny]

    def list(self, request, *args, **kwargs):
        filename = r'C:\Users\manis\Downloads\Stops_Indore.xlsx'
        filename = Path(filename)
        with open(filename, 'rb') as handle:
            df = pd.read_excel(handle)
            for index, row in df.iterrows():
                detailssave = IndoreStopsList(stopsName=row["Hawa Bangla"])
                detailssave.save()

        return Response(df, status=status.HTTP_201_CREATED)


class MatchedPlace(viewsets.ViewSet):
    permission_classes = [AllowAny]

    def list(self, request, *args, **kwargs):

        # print(request.data['place'], 'this is the value of the request data')

        # SurveyType.objects.all()
        stops = IndoreStopsList.objects.all()
        arrayofstops = []
        for stop in stops:
            arrayofstops.append(stop.stopsName)
        return Response(arrayofstops, status=status.HTTP_201_CREATED)
# TransDB viewset


class SurveyTypeViewSet(viewsets.ViewSet):
    permission_classes = [AllowAny]

    def list(self, request, *args, **kwargs):
        queryset = SurveyType.objects.all()
        serializer = TypeSerialiazer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class SurveyTypeViewFetchData(viewsets.ViewSet):
    permission_classes = [AllowAny]

    def list(self, request, *args, **kwargs):
        def generate_list_with_equal_probability(elements, length):
            num_elements = len(elements)
            weights = [1] * num_elements
            return random.choices(elements, weights=weights, k=length)
        mylist = [1, 2, 3, 4]
        result = generate_list_with_equal_probability(mylist, 1)
        if (result):
            output = TabletravelDetalis.objects.filter(
                table_used_number=result[0])
            serializer = TabletravelDetalisSerialiazer(output, many=True)
            return Response(serializer.data, status=status.HTTP_201_CREATED)


class SurveyTypeViewSettest(viewsets.ViewSet):
    permission_classes = [AllowAny]

    def list(self, request, *args, **kwargs):
        travel_details = TabletravelDetalis(
            alt1_TravelTime='25',
            alt1_TravelCost='20',
            alt1_Standing='0',
            alt1_Crowding='0',
            alt2_TravelTime='10',
            alt2_TravelCost='10',
            alt2_Standing='1',
            alt2_Crowding='5',
            used='0',
            table_used_number='4'
        )
        travel_details.save()

        # queryset = SurveyType.objects.all()
        # serializer = TypeSerialiazer(queryset, many=True)
        return Response('this is for the test purpose', status=status.HTTP_201_CREATED)


class SurveyListViewSet(viewsets.ViewSet):
    permission_classes = [AllowAny]

    def create(self, request, *args, **kwargs):
        try:
            survey_id = SurveyList.objects.all().last().surveyID+1
        except Exception as e:
            survey_id = 1
        data = {'surveyID': survey_id}
        serializer = SurveyListSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ResponseTimeViewSet(viewsets.ModelViewSet):
    queryset = ResponseTime.objects.all()
    serializer_class = ResponseTimeSerializer
    http_method_names = ['update', 'create',
                         'head', 'put', 'patch', 'options', 'post']
    permission_classes = [AllowAny]


class CollegeListViewSet(viewsets.ViewSet):
    permission_classes = [AllowAny]

    def list(self, request, *args, **kwargs):
        queryset = CollegeList.objects.all()
        serializer = CollegeListSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class FamilyViewSet(viewsets.ViewSet):
    permission_classes = [AllowAny]

    def create(self, request, *args, **kwargs):
        try:
            family_id = Family.objects.all().last().familyID+1
        except:
            family_id = 1
        data = {'familyID': family_id}
        serializer = FamilySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        # this_object_id = kwargs['familyID']
        queryset = Family.objects.all()
        family = get_object_or_404(queryset, pk=pk)
        serializer = FamilySerializer(family)
        data = []
        data.append({
            'familyID': serializer.data['familyID'],
            'currentCount': serializer.data['currentCount'],
            'noOfMembers': serializer.data['noOfMembers']
        })
        return Response(data, status=status.HTTP_201_CREATED)


class MemberViewSet(viewsets.ModelViewSet):
    permission_classes = [AllowAny]
    queryset = Member.objects.all()
    serializer_class = MemberSerializer
    http_method_names = ['update', 'create',
                         'head', 'put', 'patch', 'options', 'post']


class MemberDistrictViewSet(viewsets.ViewSet):
    permission_classes = [AllowAny]

    def create(self, request, *args, **kwargs):
        serializer = MemberDistrictSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TripViewSet(viewsets.ViewSet):
    permission_classes = [AllowAny]

    def create(self, request, *args, **kwargs):
        serializer = TripSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class OriginDestinationViewSet(viewsets.ViewSet):
    permission_classes = [AllowAny]

    def create(self, request, *args, **kwargs):
        serializer = OriginDestinationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ModeViewSet(viewsets.ViewSet):
    permission_classes = [AllowAny]

    def create(self, request, *args, **kwargs):
        serializer = ModeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class FeedbackViewSet(viewsets.ViewSet):
    permission_classes = [AllowAny]

    def create(self, request, *args, **kwargs):
        serializer = FeedbackSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ViewAllViewSet(viewsets.ViewSet):
    # authentication_classes = [SessionAuthentication, BasicAuthentication]

    # permission_classes = [IsAuthenticated, IsAdminUser]
    # permission_classes = [AllowAny]
    permission_classes = [IsAdminUser]

    def list(self, request):
        queryset = CollegeList.objects.all()
        serializer = ViewAllSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class ViewLast(viewsets.ViewSet):
    # authentication_classes = [SessionAuthentication, BasicAuthentication]

    # permission_classes = [IsAuthenticated, IsAdminUser]
    # permission_classes = [AllowAny]
    permission_classes = [IsAdminUser]

    def list(self, request):
        queryset = CollegeList.objects.all()[::-1][:1]
        serializer = ViewAllSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class PtSurveyViewSet(viewsets.ViewSet):
    permission_classes = [AllowAny]

    def create(self, request, *args, **kwargs):
        try:
            person_id = PtSurvey.objects.all().last().personID+1
        except:
            person_id = 1
        data = {'personID': person_id}
        serializer = PtSurveySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PtSurveyRatingViewSet(viewsets.ModelViewSet):
    permission_classes = [AllowAny]
    queryset = PtSurveyRating.objects.all()
    serializer_class = PtSurveyRatingSerializer
    http_method_names = ['update', 'create', 'head', 'options', 'post']


class ViewResponseTimeViewSet(viewsets.ViewSet):

    permission_classes = [IsAdminUser]

    def list(self, request):
        queryset = ResponseTime.objects.all()
        serializer = ResponseTimeSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class AQIPerceptionSurveyViewSet(viewsets.ModelViewSet):
    permission_classes = [AllowAny]
    queryset = AQIPerceptionSurvey.objects.all()
    serializer_class = AQIPerceptionSurveySerializer
    http_method_names = ['update', 'create',
                         'head', 'put', 'patch', 'options', 'post']

    # def create(self, request, *args, **kwargs):
    #     try:
    #         memberID = AQIPerceptionSurvey.objects.all().last().memberID+1
    #     except:
    #         memberID = 1
    #     data = {'memberID':memberID}
    #     serializer = AQIPerceptionSurveySerializer(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(data, status=status.HTTP_201_CREATED)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ViewAQIPerceptionSurveyViewSet(viewsets.ViewSet):

    permission_classes = [AllowAny]

    def list(self, request):
        queryset = AQIPerceptionSurvey.objects.all()
        serializer = AQIPerceptionSurveySerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class TableWillingnessViewSet(viewsets.ViewSet):
    permission_classes = [AllowAny]
    print('apiisit')

    def create(self, request, *args, **kwargs):
        print('api is hit')
        if (not request.data):
            return Response("enter any details", status=status.HTTP_400_BAD_REQUEST)
        else:
            serializer = TableWillingnessSurveyDetails(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ReadCsvFile(viewsets.ViewSet):
    def testFunction():
        return Response(status=status.HTTP_201_CREATED)
    # print('api is hit')
    # permission_classes = [AllowAny]

    # def read_csv_with_pandas(csv_file_path):
    #     # Read the CSV file into a pandas DataFrame
    #     df = df = pd.read_excel('static/ChoiceSets.xlsx', engine='openpyxl')
    #     print(df.head())
    #     return Response(status=status.HTTP_201_CREATED)
