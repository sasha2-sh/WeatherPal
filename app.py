#Copyright (c) 2026 Alexandra Folttinyová
#This program is free software under the terms of the GNU General Public License v3.
#See the LICENSE file in the project root for full terms


import requests
import os
import time


def clear():
  os.system('clear')



def fetch_response():
  location_url = "https://geocoding-api.open-meteo.com/v1/search"
  while True:
    clear()
    print('What city would you like to check weather for?')
    uI = input('> ')
    if uI:
      location_query_parameters = {'name': uI}
      location_response = requests.get(location_url, params=location_query_parameters)
      location_data = location_response.json()
      location_first_match = location_data['results'][0]
      lat = location_first_match['latitude']
      lon = location_first_match['longitude']
      weather_url = "https://api.open-meteo.com/v1/forecast"
      weather_params = {
      "latitude": lat,
      "longitude": lon,
      "current": "temperature_2m,apparent_temperature,weather_code,is_day,cloud_cover,relative_humidity_2m,precipitation,wind_speed_10m,wind_direction_10m,wind_gusts_10m,surface_pressure",
      "timezone": "auto"
      }
      weather_response = requests.get(weather_url, params=weather_params)
      weather_data = weather_response.json()
      return weather_data
    else:
      print('Please enter a city name.')

def get_variables():
  current = fetch_response()

  temperature = current["temperature_2m"]
  apparent_temp = current["apparent_temperature"]
  weather_code = current["weather_code"]
  is_day = current["is_day"]
  cloud_cover = current["cloud_cover"]
  humidity = current["relative_humidity_2m"]
  precipitation = current["precipitation"]
  wind_speed = current["wind_speed_10m"]
  wind_direction = current["wind_direction_10m"]
  wind_gusts = current["wind_gusts_10m"]
  pressure = current["surface_pressure"]

  return temperature,apparent_temp,weather_code,is_day,cloud_cover,humidity,precipitation,wind_speed,wind_direction,wind_gusts,pressure


fetch_respose()