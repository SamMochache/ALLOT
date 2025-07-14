from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, RegisterUserView

router = DefaultRouter()
router.register(r'', UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('register/', RegisterUserView.as_view(), name='register')
]