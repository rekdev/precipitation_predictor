from requests import get
from geo import get_location_data


def get_precipitation_probability_forecast(latitude, longitude):
    api_string = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&hourly=precipitation_probability&timezone=auto&forecast_days=1"

    weather_data_request = get(api_string)
    weather_data = weather_data_request.json()

    return weather_data["hourly"]


def calculate_average(precipitation_probability):
    probability_sum = 0
    forecast_hours = len(precipitation_probability)

    for hour_probability in precipitation_probability:
        probability_sum += hour_probability

    probability_average = probability_sum / forecast_hours

    return probability_average
