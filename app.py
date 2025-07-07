from precipitation import get_precipitation_probability_forecast, calculate_average
from geo import get_location_data


location_data = get_location_data()
latitude = location_data["lat"]
longitude = location_data["lon"]

probability_forecast = get_precipitation_probability_forecast(
    latitude, longitude)
average = int(calculate_average(probability_forecast))

if average > 69 and average <= 100:
    print(
        f"Precipitation probability is {average}%, it will certanly rain today, take the appropiate warnings.")
elif average > 39 and average <= 69:
    print(
        f"Precipitation probability is {average}%, so there's a medium chance it will rain, watch out and take precaution in case you have planned outdoor activities.")  
elif average >= 10 and average <= 39:
    print(
        f"Precipitation probability is {average}%, so there's a low chance it will rain.") 
elif average < 10:
    print(
        f"Precipitation probability is {average}%. so there's no chance it will rain today.")
