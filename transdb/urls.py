from django.urls import path
from . import views
from rest_framework import routers
from .api import TransDBViewSet

router = routers.DefaultRouter()

router.register('api/transdb', TransDBViewSet,'transdb' )

urlpatterns = router.urls