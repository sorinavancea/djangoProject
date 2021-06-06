from rest_framework import serializers
from .models import Weather


class WeatherSerializers(serializers.ModelSerializer):
    class Meta:
        model = Weather
        fields = ('airTemperature', 'pressure', 'humidity', 'precipitation', 'visibility', 'waterTemperature',
                  'waveDirection', 'waveHeight', 'windWaveDirection', 'windDirection', 'windSpeed', 'wavePeriod')

    class AddSerializer(serializers.ModelSerializer):
        class Meta:
            model = Weather
            fields = [
                'airTemperature',
                'pressure',
                'humidity',
                'precipitation',
                'visibility',
                'waterTemperature',
                'waveDirection',
                'waveHeight',
                'windWaveDirection',
                'windDirection',
                'windSpeed',
                'wavePeriod'
            ]

