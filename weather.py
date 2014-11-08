import pywapi as weather
ids=weather.get_location_ids(boston)
w=weather.get_weather_from_weather_com("SFXX8501",units="metric")


