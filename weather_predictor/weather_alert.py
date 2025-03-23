# For this weather alert we are using the OpenWheatherMap API & Twilio

import datetime as dt
import requests
from twilio.rest import Client

# Your Twilio account details
account_sid = "C:/Users/Razvan/Desktop/IT/keys/twilio_account_sid"
TWILIO_ACCOUNT_SID = open(account_sid, 'r').read().strip()

auth_token = "C:/Users/Razvan/Desktop/IT/keys/twilio_auth_token"
TWILIO_AUTH_TOKEN = open(auth_token, 'r').read().strip()

twilio_number = "C:/Users/Razvan/Desktop/IT/keys/twilio_phone_number"
FROM_PHONE = open(twilio_number, 'r').read().strip()
TO_PHONE = "+447367224922"         # Recepient's Phone Number
       
api_key = "C:/Users/Razvan/Desktop/IT/keys/openweathermap_api_key"
API_KEY = open(api_key, 'r').read().strip()

# Define the city and API URLs
CITY = "Milton Keynes"
BASE_URL = "https://api.openweathermap.org/data/3.0/onecall?"
forecast_url = "http://api.openweathermap.org/geo/1.0/direct?q="+ CITY + "&limit=1&appid=" + API_KEY


forecast_response = requests.get(forecast_url).json()
latitude = forecast_response[0]["lat"]
longitude = forecast_response[0]["lon"]
forc_url = f"{BASE_URL}lat={latitude}&lon={longitude}&exclude=current,minutely,hourly,alerts&appid={API_KEY}"
forc_response = requests.get(forc_url).json()
# print(forc_response)

if not forecast_response:
    raise ValueError(f"City '{CITY}' not found!")


def convert_kelvin(kelvin):
    celsius = kelvin - 273.15                 # Convert Kelvin to Celsius
    #fahrenheit = celsius * (9/15) + 32       # Convert Celsius to Fahrenheit

    return celsius

# Check for temperature
def check_temperature():
    # Get the current day and time
    now = dt.datetime.now()
    weekday = now.weekday()  # Monday is 0, Sunday is 6

    # Allow execution between 15:00 and 15:59
    if not (15 <= now.hour < 16):  
        return  # Exit if it's not between 3:00 PM and 3:59 PM
    
    # Check the forecast from the API
    for day in forc_response["daily"]:
        date = dt.datetime.fromtimestamp(day["dt"])

        # If the forecast is for today, we can use the 'eve' temperature as a substitute
        if date.date() == now.date():  # Checking if this is today
            eve_temp = convert_kelvin(day["temp"]["eve"])  # Or use day or night temp based on the forecast

            # If it's the weekday, send a notification
            if weekday < 5 and eve_temp <= 3:  # 5 = Saturday, 6 = Sunday
                send_message(f"❄️❗ Cold Temperature Alert! ⚠️\n The temperature this evening will be {eve_temp:.2f}°C in {CITY}.\nCheck the forcast for freezing temperatures!\n\n©️Razvan")
            
# Function to send Whatsapp via Twilio
def send_message(message):
    client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
    message = client.messages.create(
        body = message,
        from_ = FROM_PHONE,  # Your Twilio number with  prefix
        to = TO_PHONE     # The recipient's number with prefix
    )
    print(f"SMS message sent: {message.body}")

# Run the check
check_temperature()

