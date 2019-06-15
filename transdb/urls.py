from django.urls import path
from . import views
from rest_framework import routers
from .api import FamilyViewSet, MemberViewSet, TripViewSet, OriginDestinationViewSet, ModeViewSet

router = routers.DefaultRouter()

router.register('api/family', FamilyViewSet,'family' )

router.register('api/members', MemberViewSet,'member' )

router.register('api/trips', TripViewSet,'trip' )

router.register('api/od', OriginDestinationViewSet,'originDestination' )

router.register('api/mode', ModeViewSet,'mode' )


urlpatterns = router.urls