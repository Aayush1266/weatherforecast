import requests
import json


while(True):

    city = input("Enter the name of the city \n")
    if(city =="stop"):
        break;

    url = f"https://api.weatherapi.com/v1/current.json?key=37277b5b8ce14a92bf275828232606&q={city}"

    r = requests.get(url)

    dict = json.loads(r.text)

    print(f"{dict['location']['localtime']}")

    print(f"The current temperature of {city} is {dict['current']['temp_c']} and wind speed is {dict['current']['wind_mph']} mph")

    print(f"{dict['current']['condition']['text']}\n")
