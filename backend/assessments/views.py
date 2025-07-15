from rest_framework import viewsets, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .tasks import run_compliance_scan
from .models import Assessment, AssessmentResult
from django_filters.rest_framework import DjangoFilterBackend
from .serializers import AssessmentSerializer, AssessmentResultSerializer

class AssessmentViewSet(viewsets.ModelViewSet):
    queryset = Assessment.objects.all().order_by('created_at')
    serializer_class = AssessmentSerializer

class AssessmentResultViewSet(viewsets.ModelViewSet):
    queryset = AssessmentResult.objects.all().order_by('completed_at')
    serializer_class = AssessmentResultSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['assessment']
    ordering_fields = ['completed_at', 'risk_score']

@api_view(['POST'])
def trigger_scan(request, assessment_id):
    """
    API endpoint to trigger a compliance scan manually.
    Accepts optional 'standard' in request body: 'OWASP' (default) or 'CIS'.
    """
    standard = request.data.get('standard', 'OWASP').upper()
    
    try:
        assessment = Assessment.objects.get(pk=assessment_id)
    except Assessment.DoesNotExist:
        return Response({"error": "Assessment not found."}, status=status.HTTP_404_NOT_FOUND)
    
    run_compliance_scan.delay(assessment.id, assessment.target_system, standard)

    return Response({
        "message": f"{standard} compliance scan triggered for Assessment ID {assessment.id}",
        "target_system": assessment.target_system,
        "standard": standard
    }, status=status.HTTP_202_ACCEPTED)