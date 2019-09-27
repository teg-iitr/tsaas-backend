from django.urls import path
from . import views
from rest_framework import routers
from .api import (
    FamilyViewSet,
    MemberViewSet,
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
    )

router = routers.DefaultRouter()

# common to all survey

router.register('survey', SurveyListViewSet,'survey' )

router.register('responseTime', ResponseTimeViewSet,'surveyResponseTime' )

router.register('surveyType', SurveyTypeViewSet,'type' )

router.register('college', CollegeListViewSet,'college' )

# Household survey

router.register('family', FamilyViewSet,'family' )

router.register('members', MemberViewSet,'member' )

router.register('trips', TripViewSet,'trip' )

router.register('od', OriginDestinationViewSet,'originDestination' )

router.register('mode', ModeViewSet,'mode' )

router.register('feedback', FeedbackViewSet,'feedback' )

router.register('all', ViewAllViewSet,'all' )


# PT Survey

router.register('ptSurvey', PtSurveyViewSet,'ptSurvey' )
router.register('ptSurveyRating', PtSurveyRatingViewSet,'ptSurveyRating' )


# Survey Response Time

router.register('viewSurveyResponseTime', ViewResponseTimeViewSet,'viewSurveyResponseTime' )

urlpatterns = router.urls
