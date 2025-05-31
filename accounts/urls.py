from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views  import ProfileViewSet, UserViewSet, AddressViewSet, LogBookViewSet, LogEntryViewSet

router = DefaultRouter()
router.register(r'users', UserViewSet, basename='user')
router.register(r'profiles', ProfileViewSet, basename='profile')
router.register(r'addresses', AddressViewSet, basename='address')
router.register(r'logBook', LogBookViewSet, basename='logBook')
router.register(r'logEntry', LogEntryViewSet, basename='logEntry')

urlpatterns = [
    path('', include(router.urls))
]