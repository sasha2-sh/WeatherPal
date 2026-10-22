`temperature_2m`: Air temperature at 2 meters above ground.
`apparent_temperature`: "Feels like" temperature considering wind chill and humidity.
`weather_code`: Numeric weather condition code (WMO standard). See mapping below:
  - 0: Clear sky
  - 1: Mainly clear
  - 2: Partly cloudy
  - 3: Overcast
  - 45: Fog
  - 48: Depositing rime fog
  - 51: Drizzle (light intensity)
  - 53: Drizzle (moderate intensity)
  - 55: Drizzle (dense intensity)
  - 56: Freezing drizzle (light intensity)
  - 57: Freezing drizzle (dense intensity)
  - 61: Rain (slight intensity)
  - 63: Rain (moderate intensity)
  - 65: Rain (heavy intensity)
  - 66: Freezing rain (light intensity)
  - 67: Freezing rain (heavy intensity)
  - 71: Snow fall (slight intensity)
  - 73: Snow fall (moderate intensity)
  - 75: Snow fall (heavy intensity)
  - 77: Snow grains
  - 80: Rain showers (slight)
  - 81: Rain showers (moderate)
  - 82: Rain showers (violent)
  - 85: Snow showers (slight)
  - 86: Snow showers (heavy)
  - 95: Thunderstorm (slight or moderate)
  - 96: Thunderstorm with slight hail
  - 99: Thunderstorm with heavy hail
`is_day`: Day or night indicator (1 for day, 0 for night).
`cloud_cover`: Total cloud cover percentage.
`relative_humidity_2m`: Relative humidity percentage at 2 meters above ground.
`precipitation`: Total precipitation (rain, showers, and snow combined).
`rain`: Liquid rain amount.
`showers`: Intermittent rain shower amount.
`snowfall`: Snowfall amount.
`wind_speed_10m`: Wind speed at 10 meters above ground.
`wind_direction_10m`: Wind direction in degrees (0° = North).
`wind_gusts_10m`: Peak wind gust speed at 10 meters above ground.
`pressure_msl`: Atmospheric pressure reduced to mean sea level.
`surface_pressure`: Atmospheric pressure at ground level.