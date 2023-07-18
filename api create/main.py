from flask import Flask

app = Flask(__name__)

import requests

api_key = '2c6730a3abba1d527b7dc4e6fc949939'

user_input = input('City name :')

weather_data = requests.get(
    f"https://api.openweathermap.org/data/2.5/weather?q={user_input}&units=imperial&APPID={api_key}")

if weather_data.json()['cod'] == '404':
    print("No City Name")
else:
    weather = weather_data.json()['weather'][0]['main']
    temp = round(weather_data.json()['main']['temp'])

    print(f"The Weather in {user_input} is: {weather}")
    print(f"The temperature in {user_input} is: {temp}°F")
