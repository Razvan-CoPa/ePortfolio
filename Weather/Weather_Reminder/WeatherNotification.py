import requests
import schedule
import time

def check_weather():
    api_key = '32b46b6da8b857588a36fd4db284e706'
    city_name = input('Enter city name: ')

    url = requests.get(f"http://api.openweathermap.org/data/2.5/forecast?q={city_name}&appid={api_key}&units=metric")
    data = url.json()
    print(data)


    if url.status_code == 200:
        # Extract forecast for tonight
        tonight_forecast = None
        for forecast in data['list']:
            if 'dt_txt' in forecast and forecast['dt_txt'].split()[0] == time.strftime("%Y-%m-%d"):
                tonight_forecast = forecast
                break

        if tonight_forecast:
            temperature = tonight_forecast['main']['temp']
            print(f"Weather forecast for tonight: {city_name}") 
            print(f"Temperature: {temperature}°C")
            print(f"Description: {tonight_forecast['weather'][0]['description']}")
            print(f"Humidity: {tonight_forecast['main']['humidity']}%")
            print(f"Wind Speed: {tonight_forecast['wind']['speed']} m/s")

            if temperature < 3:
                print("Temperature is below 3°C. Consider emptying the bucket.")
        else:
            print("No forecast available for tonight.")
    else:
        print("Error:", data['message'])


# # Schedule the check_weather function to run every weekday (Monday to Friday) at 3 PM
# schedule.every().monday.to('friday').at('15:00').do(check_weather)

# # Run the scheduler loop
# while True:
#     schedule.run_pending()
#     time.sleep(1)  # Sleep for 1 second to avoid high CPU usage

check_weather()