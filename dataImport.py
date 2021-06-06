import arrow
import requests

#from polls.models import Weather
from datetime import datetime

# from polls import models
# Get first hour of today
# start = arrow.Arrow(2021,1,1,1,1,1)
# a=start.to('UTC').timestamp
# print(a)
# Get last hour of today
# end = arrow.now().ceil('day')
# print(end)
# start = 1614779317
# stop = 1622728117

start = arrow.now().floor('day')

# Get last hour of today
end = arrow.now().ceil('day')

response = requests.get(
    'https://api.stormglass.io/v2/weather/point',
    params={
        'lat': 58.7984,
        'lng': 17.8081,
        'params': ','.join(['airTemperature', 'pressure', 'humidity', 'precipitation', 'visibility', 'waterTemperature',
                            'waveDirection', 'waveHeight', 'windWaveDirection', 'windDirection', 'windSpeed',
                            'wavePeriod']),
        'source': 'sg'
    },
    headers={
        'Authorization': '328407e2-bca6-11eb-80ed-0242ac130002-32840850-bca6-11eb-80ed-0242ac130002'
    }
)


# Do something with response data.
json_data = response.json()
print(json_data)

def getData():
    return json_data