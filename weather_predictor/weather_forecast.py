# For this weather predictor we are using the OpenWheatherMap API
import datetime as dt
import requests
from zoneinfo import ZoneInfo


# Define the city and API URLs
CITY = "Milton Keynes"  # Location 
BASE_URL = "https://api.openweathermap.org/data/2.5/weather?"
BASE_URL2 = "https://api.openweathermap.org/data/3.0/onecall?"
api_key = "/Users/Razvan/Desktop/IT/keys/openweathermap_api_key"
API_KEY = open(api_key, 'r').read().strip()
url = BASE_URL + "appid=" + API_KEY + "&q=" + CITY
forecast_url = "http://api.openweathermap.org/geo/1.0/direct?q="+ CITY + "&limit=1&appid=" + API_KEY
response = requests.get(url).json()  # This response gathers the json format data about the specified city.
# print(response)

forecast_response = requests.get(forecast_url).json()
latitude = forecast_response[0]["lat"]
longitude = forecast_response[0]["lon"]
forc_url = f"{BASE_URL2}lat={latitude}&lon={longitude}&exclude=current,minutely,hourly,alerts&appid={API_KEY}"
forc_response = requests.get(forc_url).json()
# print(forc_response)

if not forecast_response:
    raise ValueError(f"City '{CITY}' not found!")


def convert_kelvin(kelvin):
    celsius = kelvin - 273.15                 # Convert Kelvin to Celsius
    #fahrenheit = celsius * (9/15) + 32       # Convert Celsius to Fahrenheit

    return celsius


temp_kelvin = response['main']['temp']
temp_celsius = convert_kelvin(temp_kelvin)
feels_like_kelvin = response['main']['feels_like']
feels_like_celsius = convert_kelvin(feels_like_kelvin)
wind_speed = response['wind']['speed']
humidity = response['main']['humidity']
clouds = response['clouds']['all']

description = response['weather'][0]['description']
local_zone = ZoneInfo("Europe/London")
date_time = dt.datetime.fromtimestamp(response['dt'], tz=dt.timezone.utc).astimezone(local_zone)
date_time = date_time.strftime('%Y-%m-%d %H:%M:%S')
sunrise_time = dt.datetime.fromtimestamp(response['sys']['sunrise'], tz=dt.timezone.utc).astimezone(local_zone).time()
sunset_time = dt.datetime.fromtimestamp(response['sys']['sunset'], tz=dt.timezone.utc).astimezone(local_zone).time()

print(f"{CITY} local date/time: {date_time}")
print(f"Temperature in {CITY}: {temp_celsius:.2f}°С, but it feels like: {feels_like_celsius:.2f}°С")
print(f"Humidity in {CITY}: {humidity}%")
print(f"Wind Speed in {CITY}: {wind_speed} m/s")
print(f"General Weather in {CITY}: {description}")
print(f"Sun rises in {CITY} at {sunrise_time} local time.")
print(f"Sun sets in {CITY} at {sunset_time} local time.")
print(f"Clouds coverage: {clouds} %")

# Request 7-day weather forecast

print(f"\n🌍 **7-Day Weather Forecast for {CITY}** 🌍\n")

# Loop through the 7-day forecast
for i, day in enumerate(forc_response["daily"][:7]):  # Get up to 7 days
    date = dt.datetime.fromtimestamp(day["dt"]).strftime('%A, %d %B %Y')
    temp_day = convert_kelvin(day["temp"]["day"])
    temp_night = convert_kelvin(day["temp"]["night"])
    humidity = day["humidity"]
    wind_speed = day["wind_speed"]
    description = day["weather"][0]["description"]
    sunrise_time = dt.datetime.fromtimestamp(day["sunrise"]).time()
    sunset_time = dt.datetime.fromtimestamp(day["sunset"]).time()

    print(f"📅 {date}")
    print(f"  🌞 Day Temp: {temp_day:.2f}°C | 🌙 Night Temp: {temp_night:.2f}°C")
    print(f"  💨 Wind: {wind_speed} m/s    | 💧 Humidity: {humidity}%")
    print(f"  ☁️ Weather: {description.capitalize()}")
    print(f"  🌅 Sunrise: {sunrise_time} | 🌇 Sunset: {sunset_time}\n")
    print("-" * 40)


for i, day in enumerate(forc_response["daily"][:7]):
    date = dt.datetime.fromtimestamp(day["dt"], tz=dt.timezone.utc).astimezone(local_zone).strftime('%A, %d %B %Y')
    sunrise_time = dt.datetime.fromtimestamp(day["sunrise"], tz=dt.timezone.utc).astimezone(local_zone).time()
    sunset_time = dt.datetime.fromtimestamp(day["sunset"], tz=dt.timezone.utc).astimezone(local_zone).time()