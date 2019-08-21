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
    ResponseTimeViewSet
    )

router = routers.DefaultRouter()

router.register('survey', SurveyListViewSet,'survey' )

router.register('surveyType', SurveyListViewSet,'type' )

router.register('responseTime', ResponseTimeViewSet,'surveyResponseTime' )

router.register('college', CollegeListViewSet,'college' )

router.register('family', FamilyViewSet,'family' )

router.register('members', MemberViewSet,'member' )

router.register('trips', TripViewSet,'trip' )

router.register('od', OriginDestinationViewSet,'originDestination' )

router.register('mode', ModeViewSet,'mode' )

router.register('feedback', FeedbackViewSet,'feedback' )

router.register('all', ViewAllViewSet,'all' )


urlpatterns = router.urls