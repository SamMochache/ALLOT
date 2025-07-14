from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ThreatViewSet

router = DefaultRouter()
router.register(r'', ThreatViewSet)

urlpatterns = [
    path('', include(router.urls)),
]