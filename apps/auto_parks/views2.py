# views.py
from rest_framework import viewsets
from .models import AutoPark, Car
from .serializers import AutoParkSerializer, CarSerializer

class AutoParkViewSet(viewsets.ModelViewSet):
    queryset = AutoPark.objects.all()
    serializer_class = AutoParkSerializer

class CarViewSet(viewsets.ModelViewSet):
    queryset = Car.objects.all()
    serializer_class = CarSerializer