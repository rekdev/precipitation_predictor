from requests import get


def get_location_data():
    localization_data = get("http://ip-api.com/json/")
    return localization_data.json()
