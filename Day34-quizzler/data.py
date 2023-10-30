import requests
API = "https://opentdb.com/api.php?amount=20&type=boolean"
response = requests.get(url=API)
response.raise_for_status()
data = response.json()
question_data = data['results']
