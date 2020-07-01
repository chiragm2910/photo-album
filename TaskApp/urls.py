from django.urls import path, include
from rest_framework import routers
from .views import AlbumViewSet, PhotoViewSet


router = routers.DefaultRouter()
router.register(r'albums', AlbumViewSet, basename='album')
router.register(r'photos', PhotoViewSet, basename='photo')

urlpatterns = [
    path(r'', include(router.urls)),
]
