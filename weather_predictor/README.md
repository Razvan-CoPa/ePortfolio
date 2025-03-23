##Weather Predictor and Alert System 🌤️📱

###Overview
This project provides a weather predictor and weather alert system using the OpenWeatherMap API to fetch weather data and Twilio to send weather-related alerts via WhatsApp.

Weather Predictor: Displays the current weather and a 7-day forecast for a given city.
Weather Alert System: Sends an alert to a designated WhatsApp number if the temperature drops below a certain threshold, notifying the user of potential freezing weather.
The weather data is retrieved using OpenWeatherMap's API, and the alerts are sent using Twilio's WhatsApp messaging service.

###Features
1. Current Weather and 7-Day Forecast
Displays the current weather for the city of your choice.
Includes temperature (Celsius), humidity, wind speed, weather description, sunrise/sunset times, and cloud coverage.
Displays a 7-day forecast, including temperature variations between day and night, wind speed, humidity, and a weather description.
2. Weather Alerts via WhatsApp
Cold Temperature Alerts: Sends an alert if the temperature is forecasted to be below 3°C on weekdays or if it's the weekend.
Sends the weather forecast details and warnings about freezing temperatures via WhatsApp.

###Requirements
Python 3.x
Python Libraries:
requests
twilio
datetime

You can install the required libraries with:

---bash---
pip install requests twilio

###Setup Instructions
1. Get API Keys
You need the following keys to run the project:

OpenWeatherMap API Key: Sign up here to get your API key.
Twilio Account SID and Auth Token: Sign up here to get your Twilio credentials for sending WhatsApp messages.

2. Add Your Keys to the Code
Ensure you replace the placeholder file paths with the actual paths where you save your API keys and Twilio credentials in the following files:

openweathermap_api_key (For OpenWeatherMap)
twilio_account_sid (For Twilio Account SID)
twilio_auth_token (For Twilio Auth Token)
twilio_whatsapp_number (Your Twilio WhatsApp number)

For example:
api_key = "/path/to/openweathermap_api_key"
account_sid = "/path/to/twilio_account_sid"
auth_token = "/path/to/twilio_auth_token"
twilio_phone_number = "/path/to/twilio_whatsapp_number"

3. Configure the Recipient's WhatsApp Number
In the weather alert code, replace TO_PHONE with the WhatsApp number where you want to receive alerts:

TO_PHONE = "+1234567890"  # Example phone number with country code



###USAGE:
Run the Weather Predictor The weather predictor will display the current weather and a 7-day forecast for the city you specify.
Example:

---bash---
python weather_predictor.py

Run the Weather Alert System The alert system checks the weather forecast and sends a WhatsApp message if the temperature is forecasted to drop below 3°C or if it’s the weekend.

Example:

---bash---
python weather_alert.py

###Code Explanation
Weather Predictor
The weather predictor code fetches data from OpenWeatherMap's API for the specified city. It retrieves:

Current weather data (temperature, humidity, wind speed, etc.).
7-day forecast data (temperature variations, wind speed, humidity).
The convert_kelvin function converts the temperature from Kelvin to Celsius.

Weather Alert System
The weather alert system code checks the forecast for a given city and sends a WhatsApp message if:

It's the weekend (Saturday/Sunday), or
The evening temperature is below or equal to 3°C on weekdays.
The check_temperature function checks the forecast and triggers the send_whatsapp_message function if conditions are met.

Sending WhatsApp Messages
The send_whatsapp_message function uses the Twilio API to send a WhatsApp message to the recipient with the weather alert.

EXAMPLE OUTPUT:
Weather Predictor:

London local date/time: 2025-03-14 14:30:00
Temperature in London: 12.34°C, but it feels like: 10.56°C
Humidity in London: 80%
Wind Speed in London: 3.5 m/s
General Weather in London: clear sky
Sun rises in London at 06:30:00 local time.
Sun sets in London at 18:45:00 local time.
Clouds coverage: 10 %

🌍 **7-Day Weather Forecast for London** 🌍

📅 Monday, 15 March 2025
  🌞 Day Temp: 15.50°C | 🌙 Night Temp: 8.40°C
  💨 Wind: 2.0 m/s    | 💧 Humidity: 75%
  ☁️ Weather: clear sky
  🌅 Sunrise: 06:25:00 | 🌇 Sunset: 18:40:00

----------------------------------------

ALERT EXAMPLE:
WhatsApp message sent: ❄️❗ Cold Temperature Alert! ⚠️
The temperature this evening will be 2.5°C in London.
Check the forecast for freezing temperatures!

©️Razvan


Contribution
Feel free to fork and contribute to this project! Open issues for suggestions, improvements, or new features.

License
This project is licensed under the MIT License.