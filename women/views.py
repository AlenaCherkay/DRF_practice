from django.shortcuts import render

from rest_framework import generics
from .models import Women, Category
from .serializers import WomenSerializer

# ListAPIView – чтение списка данных по GET-запросу
class WomenAPIView(generics.ListAPIView):
    queryset = Women.objects.all()
    serializer_class = WomenSerializer


# ListCreateAPIView – для чтения (по GET-запросу) и создания списка данных (по POST-запросу)
class WomenAPIList(generics. ListCreateAPIView):
    queryset = Women.objects.all()
    serializer_class = WomenSerializer
