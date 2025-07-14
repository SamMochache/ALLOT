from rest_framework import viewsets, generics
from .models import User
from .serializers import UserSerializer, RegisterSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class RegisterUserView(generics.CreateAPIView):
    serializer_class = RegisterSerializer
    queryset = User.objects.all()