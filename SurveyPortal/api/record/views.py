# Create your views here.
from .serializers import RecordSerializer
from rest_framework import viewsets
from .models import Record

# Create your views here.

class RecordViewSet(viewsets.ModelViewSet):
  queryset = Record.objects.all()
  serializer_class = RecordSerializer