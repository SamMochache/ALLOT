from rest_framework import viewsets
from .models import Vulnerability
from .serializers import VulnerabilitySerializer

class VulnerabilityViewSet(viewsets.ModelViewSet):
    queryset = Vulnerability.objects.all()
    serializer_class = VulnerabilitySerializer