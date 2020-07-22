import requests

def fetchWeatherinfo(city):
    api_address = 'http://api.openweathermap.org/data/2.5/weather?APPID=3d940b28bf71ac826aee0be5e5582ba4&q='
    # city = input('Enter the City Name :')
    city_lowercase = str(city)
    print("I am from weather.py"+ city_lowercase.lower())
    url = api_address + city_lowercase
    json_data = requests.get(url).json()
    format_add = json_data['main']
    print(format_add)
    print("Weather forecast is {0}..Minimum temperature is {1} Celsius. Maximum Temperature is {2} Celsius".format(
        json_data['weather'][0]['main'],int(format_add['temp_min']-273),int(format_add['temp_max']-272)))
    return format_add