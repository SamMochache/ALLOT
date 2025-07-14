from rest_framework import viewsets
from .models import Threat
from .serializers import ThreatSerializer

class ThreatViewSet(viewsets.ModelViewSet):
    queryset = Threat.objects.all()
    serializer_class = ThreatSerializer