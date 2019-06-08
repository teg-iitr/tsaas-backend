from transdb.models import TransDB
from rest_framework import viewsets, permissions
from .serializers import TransDBSerializer

# TransDB viewset
class TransDBViewSet(viewsets.ModelViewSet):
    queryset = TransDB.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = TransDBSerializer