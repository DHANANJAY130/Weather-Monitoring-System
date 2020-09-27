import requests
import json

apikey = open("apikey.txt", 'r').readline().strip()

cityname = input("Enter City name: ")

complete_url = f"http://api.openweathermap.org/data/2.5/weather?q={cityname}&appid={apikey}"

reponse = requests.get(complete_url)

weather_data = reponse.json()

if weather_data["cod"] != "404":
    data = weather_data["main"]
    print(f"Weather details of ", weather_data["name"])
    temp = data["temp"]
    print(f"Current temperature is: {int(temp)-273} degree Celcius")

    desc = weather_data["weather"][0]["description"]
    print(f"Weather Description:\n {desc}")
else:
    print("City Not found, make sure you typed the city name correctly.\n")