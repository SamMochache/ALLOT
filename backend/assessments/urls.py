from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AssessmentViewSet, AssessmentResultViewSet, trigger_scan

router = DefaultRouter()
router.register(r'assessment-results', AssessmentResultViewSet)
router.register(r'', AssessmentViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('trigger-scan/<int:assessment_id>/', trigger_scan, name='trigger-scan'),
]