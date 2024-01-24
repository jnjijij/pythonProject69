# models.py
from django.db import models
from django.contrib.auth.models import User

class AutoPark(models.Model):
    name = models.CharField(max_length=100)
    user = models.ForeignKey(User, related_name='auto_parks', on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Car(models.Model):
    auto_park = models.ForeignKey(AutoPark, related_name='cars', on_delete=models.CASCADE)
    make = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    year = models.IntegerField()
    color = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.year} {self.make} {self.model}"