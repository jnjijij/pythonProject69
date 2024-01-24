# urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AutoParkViewSet, CarViewSet

router = DefaultRouter()
router.register(r'autoparks', AutoParkViewSet)
router.register(r'cars', CarViewSet)

urlpatterns = [
    path('', include(router.urls)),
    # Add other URL patterns as needed
]