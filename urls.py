from django.contrib import admin
from django.urls import include, path

from app.views import WeatherListView

urlpatterns = [
    path('', WeatherListView.as_view())
]