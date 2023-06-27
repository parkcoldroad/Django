from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import EssayViewSet

router = DefaultRouter()
router.register('essay', EssayViewSet)

urlpatterns = [
    path('', include(router.urls))
]
