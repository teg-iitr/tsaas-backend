from django.shortcuts import render

# Create your views here.
from transdb.models import TransDB
from transdb.serializers import TransDBSerializer
from rest_framework import viewsets

class TransDBListCreate(viewsets.ModelViewSet):
    queryset = TransDB.objects.all()
    serializer_class = TransDBSerializer
