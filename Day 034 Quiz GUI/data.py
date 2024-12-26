import requests

parameters = {
    "amount": 10,
    "type": "boolean"
}

request = requests.get("https://opentdb.com/api.php", params=parameters)
request.raise_for_status()
data = request.json()
question_data = data["results"]

