import requests
import datetime

city = "Dubai"
weather = {'cloud_pct': 55, 'temp': 37, 'feels_like': 44, 'humidity': 53, 'min_temp': 36, 'max_temp': 37, 'wind_speed': 6.17, 'wind_degrees': 310, 'sunrise': 1695262006, 'sunset': 1695305848}

def weather_cloud():
    if weather['cloud_pct'] > 30 and weather['cloud_pct'] < 60:
        print ("It's partially cloudy in", city,)
    elif weather['cloud_pct'] >= 60:
        print (f"It's cloudy in {city} with a cloud coverage of {weather['cloud_pct']}%")
    else:
        print ("It's sunny in", city)

def weather_temp():
    if weather['temp'] != weather["feels_like"]:
        print (f"the temperature is currently at {weather['temp']}°C but feels like {weather['feels_like']} °C")
    else:
        print (f"the temperature is currently at {weather['temp']}°C")
    print (f"The temperature range today will be between {weather['min_temp']}°C and {weather['max_temp']}°C")

def weather_humid():
    print (f"Humidity level is at {weather['humidity']}%")

def weather_wind():
    degrees = weather["wind_degrees"]
    cardinals = ["Northern", "Northeastern", "Eastern", "Southeastern", "Southern", "Southwestern", "Western", "Northwestern", "Northern"]
    cardinal = cardinals[round(degrees / 45)]
    print (F"There's a {cardinal} wind at {weather['wind_speed']} meters per second")

def weather_sun():
    sunrise_timestamp = weather['sunrise']
    sunset_timestamp = weather['sunset']

    sunrise_datetime = datetime.datetime.utcfromtimestamp(sunrise_timestamp)
    sunset_datetime = datetime.datetime.utcfromtimestamp(sunset_timestamp)

    print(f"Today the sun rises in {city} at {sunrise_datetime.strftime('%H:%M')} (UTC) and sets at {sunset_datetime.strftime('%H:%M')}")
    

weather_cloud()
print("-"*62)
weather_temp()
print("-"*62)
weather_wind()
print("-"*62)
weather_humid()
print("-"*62)
weather_sun()



# {"cloud_pct": 75, "temp": 17, "feels_like": 16, "humidity": 70, "min_temp": 14, "max_temp": 18, "wind_speed": 2.06, "wind_degrees": 0, "sunrise": 1695275057, "sunset": 1695319397}