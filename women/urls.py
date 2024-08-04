from django.urls import path
from .views import WomenAPIView, WomenAPIList

urlpatterns = [
    path('drf/', WomenAPIView.as_view()),
    path('drf-list', WomenAPIList.as_view()),
]