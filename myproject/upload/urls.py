from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ImageViewSet , DocumentationViewSet

router = DefaultRouter()
router.register('images', ImageViewSet)
router.register('files', DocumentationViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
