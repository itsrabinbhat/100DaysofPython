import requests
from twilio.rest import Client
city = 'Toronto'
api_key = "100a91d50abe7cad233cc99a33608cd9"
API = f"https://api.openweathermap.org/data/2.5/forecast"
api_param = {
    "lat": 43.653225,
    "lon": -79.383186,
    "appid": api_key,
    "cnt": 4
}
account_sid = 'AC1ea464d0ab8bc481aa2b277996e5f4b6'
auth_token = '1c9a62190af76e70dba2a9240de66b36'

response = requests.get(url=API, params=api_param)
response.raise_for_status()
data = response.json()

# Creating a list of weather id for each interval
weather_ids = []
for each_interval in data['list']:
    for weather in each_interval['weather']:
        weather_ids.append(weather['id'])

# Checking if you need an umbrella
will_rain = False
for each_id in weather_ids:
    if each_id < 700:
        will_rain = True

# Sending alerts
if True:
    client = Client(account_sid, auth_token)

    message = client.messages.create(
        body="It's going to rain today, Don't forget your ☔.",
        from_='+14063441679',
        to='+16479367307'
    )

    print(message.status)
