import requests
SHEETY_API = "https://api.sheety.co/9b6ab3bb9610ea401e7f0c6579f59cff/flightDeals/sheet1"


class DataManager:
    def __init__(self):
        self.destination_data = {}

    def get_sheety_data(self):
        res = requests.get(url=SHEETY_API)
        data = res.json()
        self.destination_data = data['sheet1']
        return self.destination_data

    def update_destination_code(self):
        for city in self.destination_data:
            new_data = {
                'sheet1': {
                    'iataCode': city['iataCode']
                }
            }

            res = requests.put(
                url=f"{SHEETY_API}/{city['id']}",
                json=new_data
            )

            print(res.status_code)


