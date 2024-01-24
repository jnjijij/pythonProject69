# serializers.py
from rest_framework import serializers
from .models import AutoPark, Car

class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = ['make', 'model', 'year', 'color']

class AutoParkSerializer(serializers.ModelSerializer):
    cars = CarSerializer(many=True, read_only=True)

    class Meta:
        model = AutoPark
        fields = ['id', 'name', 'cars']