from django.urls import path
from . import views
from rest_framework import routers
from .api import (
    FamilyViewSet,
    MemberViewSet,
    MemberDistrictViewSet,
    ReadCsvFile,
    TripViewSet,
    OriginDestinationViewSet,
    ModeViewSet,
    ViewAllViewSet,
    CollegeListViewSet,
    FeedbackViewSet,
    SurveyListViewSet,
    ResponseTimeViewSet,
    SurveyTypeViewSet,
    PtSurveyViewSet,
    PtSurveyRatingViewSet,
    ViewResponseTimeViewSet,
    ViewLast,
    SurveyTypeViewFetchData,
    AQIPerceptionSurveyViewSet,
    ViewAQIPerceptionSurveyViewSet, SurveyTypeViewSettest, TableWillingnessViewSet,
    ReadIndoreCsv,
    MatchedPlace,
    ReadWillingnessData
)


router = routers.DefaultRouter()


# for willingness survey
router.register('willingnessdata', ReadWillingnessData, 'willingnessdata')
router.register('indorecsv', ReadIndoreCsv, 'indorecsv')
router.register('place', MatchedPlace, 'place')
# common to all survey

router.register('data', SurveyTypeViewFetchData, 'data')

router.register('test', SurveyTypeViewSettest, 'test')

router.register('survey', SurveyListViewSet, 'survey')

router.register('responseTime', ResponseTimeViewSet, 'surveyResponseTime')

router.register('surveyType', SurveyTypeViewSet, 'type')

router.register('college', CollegeListViewSet, 'college')

# Household survey

router.register('family', FamilyViewSet, 'family')

router.register('members', MemberViewSet, 'member')

router.register('member-district', MemberDistrictViewSet, 'member-district')

router.register('trips', TripViewSet, 'trip')

router.register('od', OriginDestinationViewSet, 'originDestination')

router.register('mode', ModeViewSet, 'mode')

router.register('feedback', FeedbackViewSet, 'feedback')

router.register('all', ViewAllViewSet, 'all')

router.register('last', ViewLast, 'last')


# PT Survey

router.register('ptSurvey', PtSurveyViewSet, 'ptSurvey')
router.register('ptSurveyRating', PtSurveyRatingViewSet, 'ptSurveyRating')


# Survey Response Time

router.register('viewSurveyResponseTime',
                ViewResponseTimeViewSet, 'viewSurveyResponseTime')

# AQI Perception Survey


router.register('read', ReadCsvFile, 'read')

router.register('aqips', AQIPerceptionSurveyViewSet, 'aqiPerceptionSurvey')
router.register('viewAQIPSResponses',
                ViewAQIPerceptionSurveyViewSet, 'viewAQIPSResponses')


# willingnessSurvey
router.register('TableWillingnessSurveyDetails',
                TableWillingnessViewSet, 'TableWillingnessSurveyDetails')

urlpatterns = router.urls
