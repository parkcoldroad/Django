from django.urls import path
from . import views

urlpatterns = [
    path('show-map/', views.show_map),
]
