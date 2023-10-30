import requests
import smtplib
from datetime import datetime as dt
MY_LAT = 43.653225
MY_LNG = -79.383186
EMAIL = 'test.rbhat@gmail.com'
PASSWORD = 'enregiarlbtffjmh'

parameters = {
    'lat': MY_LAT,
    'lng': MY_LNG,
    'formatted': 0
}

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
iss_lat = float(response.json()['iss_position']['latitude'])
iss_lng = float(response.json()['iss_position']['longitude'])

response = requests.get(url='https://api.sunrise-sunset.org/json', params=parameters)
response.raise_for_status()
data = response.json()
sunrise = int(data['results']['sunrise'].split('T')[1].split(':')[0])
sunset = int(data['results']['sunset'].split('T')[1].split(':')[0])

current_time = dt.now().hour

if current_time > sunset or current_time < sunrise:
    if int(iss_lat) in range(int(MY_LAT)-5, int(MY_LAT)+5) and int(iss_lng) in range(int(MY_LNG)-5, int(MY_LNG)+5):
        with smtplib.SMTP('smtp.gmail.com', port=587) as connection:
            connection.starttls()
            connection.login(EMAIL, PASSWORD)
            connection.sendmail(EMAIL, 'itsrabio7@gmail.com', msg=f"Subject: Position of ISS!\n\nLook up!"
                                                                  f"\nISS is passing by above you.")
