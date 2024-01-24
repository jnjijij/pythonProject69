# urls.py
from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import AutoParkViewSet, CarViewSet, UserProfileViewSet

router = DefaultRouter()
router.register(r'autoparks', AutoParkViewSet)
router.register(r'cars', CarViewSet)
router.register(r'users', UserProfileViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    # Add other URL patterns as needed
]