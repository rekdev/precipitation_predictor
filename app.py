import os
from datetime import datetime
from precipitation import get_precipitation_probability_forecast, calculate_average
from geo import get_location_data


def clear_screen():
    if os.name == "posix":
        os.system("clear")
    else:
        os.system("cls")


def get_advice(average):
    if average < 10:
        print(
            "> Even though chance of raining is low, it doesn't guarantee a rain-free day.")
    elif average >= 10 and average <= 39:
        print("> There's a low chance of precipitation, though there's still a chance for some drizzle in some areas.")
    elif average > 39 and average <= 69:
        print("! > There's a medium chance for raining, watch out and take the necesarly preparations in case you've planned outdoor activities.")
    elif average > 69 and average <= 100:
        print(
            "! > Take the necesarly preparations, such as carrying an umbrella or raincoat.")


location_data = get_location_data()
city = location_data["city"]
country = location_data["country"]
latitude = location_data["lat"]
longitude = location_data["lon"]
breakpoint()

probability_forecast = get_precipitation_probability_forecast(
    latitude, longitude)

precipitation_probability = probability_forecast["precipitation_probability"]
time = probability_forecast["time"]

average = round(calculate_average(precipitation_probability))

while True:
    breakpoint()
    clear_screen()
    print(f"{city}, {country}: Average precipitation probability: {average}%")

    get_advice(average)

    option = int(
        input("Insert an option 1) Get hourly today forecast 2) Exit: "))

    if option == 1:
        clear_screen()

        for i in range(24):
            dt = datetime.fromisoformat(time[i])

            print(f"{dt}: {precipitation_probability[i]}%")
            print("-------------------------")

        input(": ")

    elif option == 2:
        break
