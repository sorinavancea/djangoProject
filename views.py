from datetime import datetime, timedelta
from pprint import pprint

from django.shortcuts import render
import requests
# Create your views here.
from rest_framework.generics import ListAPIView, CreateAPIView
from app.models import Weather
from .serializers import WeatherSerializers
from .dataImport import getData

class WeatherListView(ListAPIView):
    queryset = Weather.objects.all()
    serializer_class = WeatherSerializers
    pprint(getData())

class WeatherCreateAPIView(CreateAPIView):
    queryset = Weather.objects.all()
    serializer_class = WeatherSerializers
    getData()
    pprint(getData())
