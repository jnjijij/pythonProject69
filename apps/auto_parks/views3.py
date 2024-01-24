# views.py
from rest_framework import viewsets
from .models import AutoPark, Car, UserProfile
from .serializers import AutoParkSerializer, CarSerializer, UserProfileSerializer

class AutoParkViewSet(viewsets.ModelViewSet):
    queryset = AutoPark.objects.all()
    serializer_class = AutoParkSerializer

class CarViewSet(viewsets.ModelViewSet):
    queryset = Car.objects.all()
    serializer_class = CarSerializer

class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer