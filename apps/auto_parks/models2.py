from django.db import models
from django.contrib.auth.models import User

class AutoPark(models.Model):
    name = models.CharField(max_length=100)
    user = models.ForeignKey(User, related_name='auto_parks', on_delete=models.CASCADE)

    # Add more fields as needed